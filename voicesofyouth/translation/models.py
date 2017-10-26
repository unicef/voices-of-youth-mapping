"""
The VoY project need the data have translation for some records, this app will help us in this task.
"""
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from psycopg2 import ProgrammingError

from .fields import CharFieldTranslatable
from .fields import TextFieldTranslatable

__author__ = ['Elton Pereira', ]
__email__ = 'eltonplima AT gmail DOT com'
__status__ = 'Development'


class TranslatableModel(models.Model):
    """
    Stores which model that have fields that can be translated.

    Attributes:
        model: Model name.
        verbose_name: Verbose name from model.
        verbose_name_plural: Plural version of verbose name.
    """
    model = models.CharField(max_length=128)
    verbose_name = models.CharField(max_length=128)
    verbose_name_plural = models.CharField(max_length=128)

    def __str__(self):
        return self.model


class TranslatableField(models.Model):
    """
    Stores which fields that can be translated.

    Attributes:
        model: Model TranslatableModel instance.
        field: Name of the field.
        verbose_name: Verbose name of the field.
    """
    model = models.ForeignKey(TranslatableModel)
    field_name = models.CharField(max_length=128)
    verbose_name = models.CharField(max_length=128)

    class Meta:
        unique_together = ('model', 'field_name')

    def __str__(self):
        return f'{self.model}.{self.verbose_name}'


class TranslationManager(models.Manager):
    def get_translations_for_model(self, model_instance, lang_code=None):
        qs = self.get_queryset()
        ct = ContentType.objects.get_for_model(model_instance)
        filter_clauses = {
            'content_type': ct,
            'object_id': model_instance.id
        }
        if lang_code is not None:
            filter_clauses['lang_code'] = lang_code
        return qs.filter(**filter_clauses)

    def translate_object(self, model_instance, lang_code):
        """
        Apply the translation for fields values if exists, otherwise do nothing.

        The translation is applied directly in the model_instance fields.

        Attributes:
            model_instance: Model instance.
            lang_code: Language code used to translate.
        """
        content_type = ContentType.objects.get_for_model(model_instance._meta.model)
        translations = self.get_queryset().filter(language=lang_code,
                                                  content_type=content_type,
                                                  object_id=model_instance.id)
        for translation in translations:
            setattr(model_instance, translation.field.field_name, translation.translation)


class Translation(models.Model):
    """
    Stores the translation.

    Attributes:
        field: TranslatableField instance.
        language: What is the language of this translation.
        translation: Translation itself.
        content_type: Content type of the original model instance(**you don't need to manipulate this field**).
        object_id: ID of the original model instance(**you don't need to manipulate this field**).
        content_object: Object instance itself.
    """
    field = models.ForeignKey(TranslatableField)
    language = models.CharField(max_length=8, choices=settings.LANGUAGES)
    translation = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    objects = TranslationManager()

    class Meta:
        unique_together = ('language', 'field', 'content_type', 'object_id')
        ordering = ('language', )

    def __str__(self):
        return f'{self.field}({self.language})'


# Store the fields that need translation.
translatable_fields = []


def is_translatable_model(model):
    translatable = False
    for field in model._meta.get_fields():
        if type(field) in (CharFieldTranslatable, TextFieldTranslatable):
            translatable = True
            break
    return translatable


def create_translatable_model(model, create_fields=True):
    if is_translatable_model(model):
        data = {'model': model._meta.model_name,
                'verbose_name': model._meta.verbose_name,
                'verbose_name_plural': model._meta.verbose_name_plural}
        model_instance = TranslatableModel.objects.update_or_create(**data, defaults=data)[0]
        for field in model._meta.get_fields():
            if type(field) in (CharFieldTranslatable, TextFieldTranslatable):
                translatable_fields.append({'model': model_instance,
                                            'field_name': field.attname,
                                            'verbose_name': field.verbose_name})
        if create_fields:
            create_translatable_fields()


def create_translatable_fields():
    while len(translatable_fields) > 0:
        field_data = translatable_fields.pop(0)
        TranslatableField.objects.update_or_create(model=field_data['model'],
                                                   field_name=field_data['field_name'],
                                                   defaults=field_data)


@receiver(post_migrate)
def create_translations(app_config, **_):
    """
    Populates the translation app models with all models that use the fields CharFieldTranslatable or
    TextFieldTranslatable.

    .. note::
        This function is called when migrate runs.
    """
    if settings.PROJECT_NAME in app_config.name:
        for model in app_config.get_models():
            if is_translatable_model(model):
                print("{:=^80}".format(f' Translatable fields '))
                print("{:-^80}".format(f' {app_config.name}.{model.__name__} '))
                create_translatable_model(model, False)
                for field in translatable_fields:
                    print(field['field_name'])
        try:
            TranslatableModel.objects.all()
            create_translatable_fields()
        except ProgrammingError:
            """
            If this exception occur here, is because the translation app migration has not yet performed.
            """
