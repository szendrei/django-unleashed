from django import forms
from django.core.exceptions import ValidationError
from django.utils.text import slugify

from .models import Snippet


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        exclude = ["create_date", ]

    def clean_slug(self):
        new_slug = (self.cleaned_data['slug'].lower())
        if new_slug == 'create':
            raise ValidationError('Slug may not be "create".')
        if not new_slug:
            new_slug = ''
        return new_slug
