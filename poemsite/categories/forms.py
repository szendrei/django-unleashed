from django import forms
from .models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

    def clean_slug(self):
        new_slug = self.cleaned_data["slug"].lower()
        if new_slug == "create":
            raise ValidationError('Slug may not be "create".')
        return new_slug
