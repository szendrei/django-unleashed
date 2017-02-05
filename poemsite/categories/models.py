from django.db import models
from django.core.urlresolvers import reverse


class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)
    slug = models.CharField(max_length=32, unique=True, 
                            help_text='A label for URL config.')

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return reverse('categories_category_detail',kwargs={'slug':self.slug})

    def get_update_url(self):
        return reverse('categories_category_update',kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse('categories_category_delete', kwargs={'slug':self.slug})

    class Meta:
        ordering=["name"]
        verbose_name_plural = "categories"
