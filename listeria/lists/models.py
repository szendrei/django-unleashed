from django.db import models
from django.core.urlresolvers import reverse


class List(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(max_length=63,help_text='A label for URL config',
                            unique=True)
    pub_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering=['-pub_date']
        get_latest_by= 'pub_date'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lists_list_detail',kwargs={'slug':self.slug})


class Item(models.Model):
    text = models.TextField()
    parent_list = models.ForeignKey(List, on_delete=models.CASCADE)
    ordering = models.PositiveSmallIntegerField(default=1)

    class Meta:
        ordering=["ordering"]
        unique_together = ('ordering', 'parent_list')

    def __str__(self):
        return "{} in {}".format(self.text, parent_list)
