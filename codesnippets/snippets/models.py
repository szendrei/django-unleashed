from django.db import models
from pygments.lexers import get_all_lexers
from django.core.urlresolvers import reverse

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])


class Snippet(models.Model):
    create_date = models.DateTimeField('created date', auto_now_add=True)
    title = models.CharField(max_length=63, blank=True, default='')
    code = models.TextField()
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python',
                                max_length=100)
    author = models.CharField(max_length=32, blank=True, default='Anonymus')
    slug = models.CharField(max_length=63, unique=True, blank=True, default='')

    class Meta:
        ordering = ['-create_date']

    def __str__(self):
        if len(self.title):
            return self.title
        else:
            return "{} code created at {}".format(self.language, 
                                                  self.create_date)

    def get_absolute_url(self):
        return reverse('snippets_snippet_detail',kwargs={'slug':self.slug})

    def get_category_url(self):
        return reverse('snippets_snippet_category_list',
                       kwargs={'language':self.language})

    def get_update_url(self):
        return reverse('snippets_snippet_update',kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse('snippets_snippet_delete',kwargs={'slug':self.slug})
