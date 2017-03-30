from django import forms
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from .models import Item, List

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ListForm, self).__init__(*args, **kwargs)
        self.fields['slug'].required=False

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug my not be "create".')
        if not new_slug:
            new_slug = slugify(self.cleaned_data['title'])
        return new_slug


class ItemCreateForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ['ordering']


class ItemUpdateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"
