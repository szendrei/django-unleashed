from django.conf.urls import url
from .views import (snippet_list, snippet_list_category, snippet_detail, 
                    SnippetCreate, SnippetUpdate, SnippetDelete)

urlpatterns = [
    url(r'^$', snippet_list, name='snippets_snippet_list'),
    url(r'^list/(?P<language>[\w\-]+)/$', snippet_list_category, 
        name='snippets_snippet_category_list'),
    url(r'^create/$', SnippetCreate.as_view(), name="snippets_snippet_create"),
    url(r'^(?P<slug>[\w\-]+)/$', snippet_detail, 
        name='snippets_snippet_detail'),
    url(r'^(?P<slug>[\w\-]+)/update/$', SnippetUpdate.as_view(), 
        name='snippets_snippet_update'),
    url(r'^(?P<slug>[\w\-]+)/delete/$', SnippetDelete.as_view(), 
        name='snippets_snippet_delete'),
]
