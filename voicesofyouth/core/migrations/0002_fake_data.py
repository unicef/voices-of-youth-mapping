# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 18:54
import random

from django.conf import settings
from django.core.files.images import ImageFile
from django.db import migrations
from model_mommy import mommy
from model_mommy.random_gen import gen_string
from unipath import Path
import lorem

from voicesofyouth.project.models import Project
from voicesofyouth.report.models import Report
from voicesofyouth.theme.models import Theme
from voicesofyouth.translation.fields import CharFieldTranslatable, TextFieldTranslatable
from voicesofyouth.translation.models import Translation

__author__ = 'Elton Pereira'
__email__ = 'eltonplima AT gmail DOT com'
__status__ = 'Development'

mommy.generators.add(TextFieldTranslatable, gen_string)
mommy.generators.add(CharFieldTranslatable, gen_string)


def create_dev_data(apps, schema_editor):
    if settings.DEBUG:
        test_img = Path(__file__).absolute().ancestor(3).child('test', 'assets', 'python.png')
        with open(test_img, 'rb') as image:
            tags = ('trash',
                    'healthy',
                    'security',
                    'harzadous area',
                    'climate changes',
                    'star wars',
                    'crazy',
                    'anything')
            fake_thumbnail = ImageFile(image)
            for x in range(random.randint(5, 10)):
                project = mommy.make(Project,
                                     name=f'Project {x}',
                                     thumbnail=fake_thumbnail,
                                     description=lorem.paragraph())
                for y in range(random.randint(5, 10)):
                    theme = mommy.make(Theme, project=project, name=f'Theme {y}', description=lorem.paragraph())
                    theme.tags.add(*random.choices(tags, (len(t) for t in tags), k=random.randint(1, 6)))
                    lang_idx = random.randint(0, len(settings.LANGUAGES) - 1)
                    mommy.make(Translation, content_object=theme, language=settings.LANGUAGES[lang_idx][0])
                    mommy.make(Translation, content_object=project, language=settings.LANGUAGES[lang_idx][0])
                    mommy.make(Translation, content_object=theme, language='en')
                    mommy.make(Translation, content_object=project, language='en')
                    for z in range(random.randint(1, 10)):
                        report = mommy.make(Report, name=f'Report {z}', description=lorem.paragraph(), theme=theme)
                        report.tags.add(*random.choices(tags, (len(t) for t in tags), k=random.randint(1, 6)))


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('project', '0002_auto_20171023_1906'),
        ('theme', '0002_auto_20171023_1906'),
        ('tag', '0001_initial'),
        ('translation', '0001_initial'),
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_dev_data)
    ]
