from django.db import models
from django.core.urlresolvers import reverse
from categories.models import Category


class Poem(models.Model):
    title = models.CharField(max_length=32)
    author = models.CharField(max_length=63)
    slug = models.SlugField(unique=True,help_text='A label for URL config.')
    pub_date = models.DateField('date published', auto_now_add=True)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, 
                                 related_name="poems")

    def __str__(self):
        return "{} by {}".format(self.title, self.author)

    def get_absolute_url(self):
        return reverse('poems_poem_detail',kwargs={'slug':self.slug})

    def get_update_url(self):
        return reverse('poems_poem_update',kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse('poems_poem_delete',kwargs={'slug':self.slug})

    class Meta:
        ordering=['-pub_date']
        get_latest_by='pub_date'
        unique_together = ('title', 'author')
