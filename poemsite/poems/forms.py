from django import forms
from .models import Poem


class PoemForm(forms.ModelForm):
    class Meta:
        model = Poem
        exclude = ['pub_date']

    def clean_slug(self):
        new_slug = (self.cleaned_data['slug'].lower())
        if new_slug == 'create':
            raise ValidationError('Slug may not be "create".')
        return new_slug

