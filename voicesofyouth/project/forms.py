from django import forms
from django.conf import settings as django_settings
from django.utils.translation import ugettext as _

from leaflet.forms.fields import PolygonField

from .models import Project

from voicesofyouth.user.models import VoyUser

from voicesofyouth.translation.forms import TranslationsField

class ProjectForm(forms.Form):
    name = forms.CharField(
        label=_('Name'),
        required=True,
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Add a project name'),
                'required': True,
                'class': 'form-control',
            }
        )
    )

    description = forms.CharField(
        label=_('Path'),
        required=True,
        widget=forms.Textarea(
            attrs={
                'required': True,
                'class': 'form-control',
            }
        )
    )

    language = forms.ChoiceField(
        choices=django_settings.LANGUAGES,
        label=_('Language'),
        required=True,
        widget=forms.Select(
            attrs={
                'required': True,
                'class': 'form-control',
            }
        )
    )

    path = forms.CharField(
        label=_('Path'),
        required=False,
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Path'),
                'required': False,
                'class': 'form-control',
            }
        )
    )

    bounds = PolygonField(
        required=True
    )

    tags = forms.CharField(
        label=_('Tags'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'required': True,
                'class': 'form-control',
            }
        )
    )

    local_admin = forms.ModelMultipleChoiceField(
        queryset=None,
        label=_('Local Admin'),
        required=True,
        widget=forms.SelectMultiple(
            attrs={
                'required': True,
                'multiple': True,
                'class': 'form-control',
            }
        )
    )

    thumbnail = forms.FileField(
        label=_('Thumbnail'),
        required=False,
        widget=forms.ClearableFileInput(
            attrs={
                'required': False,
                'class': 'form-control',
            }
        )
    )

    enabled = forms.BooleanField(
        label=_('Enabled'),
        required=False
    )

    translations = TranslationsField(
        Project,
        label=_('Languages'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'required': True,
                'class': 'form-control',
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['local_admin'].queryset = VoyUser.objects.all()

    def clean(self):
        cleaned_data = super(ProjectForm, self).clean()
        bounds = cleaned_data.get('bounds')

        if bounds is None:
            raise forms.ValidationError(_('Bounds is empty'))


class ProjectTranslationForm(forms.Form):
    language = forms.ChoiceField(
        choices=django_settings.LANGUAGES,
        label=_('Language'),
        required=True,
        widget=forms.Select(
            attrs={
                'required': True,
                'class': 'form-control',
            }
        )
    )

    name = forms.CharField(
        label=_('Name'),
        required=True,
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'required': True,
                'class': 'form-control',
            }
        )
    )

    description = forms.CharField(
        label=_('Description'),
        required=True,
        widget=forms.Textarea(
            attrs={
                'required': True,
                'class': 'form-control',
            }
        )
    )
