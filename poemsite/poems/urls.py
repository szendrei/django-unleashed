from django.conf.urls import url
from .views import poem_list, poem_detail, PoemCreate, PoemUpdate, PoemDelete

urlpatterns = [
    url(r'^$', poem_list, name='poems_poem_list'),
    url(r'^create/$', PoemCreate.as_view(), name='poems_poem_create'),
    url(r'^(?P<slug>[\w\-]+)/$', poem_detail, name='poems_poem_detail'),
    url(r'^(?P<slug>[\w\-]+)/update/$', PoemUpdate.as_view(), 
        name='poems_poem_update'),
    url(r'^(?P<slug>[\w\-]+)/delete/$', PoemDelete.as_view(), 
        name='poems_poem_delete'),
]
