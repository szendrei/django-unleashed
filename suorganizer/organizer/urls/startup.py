from django.conf.urls import url
from ..views import (NewsLinkCreate, NewsLinkDelete, NewsLinkUpdate,
                     StartupCreate, StartupUpdate, StartupDelete, 
                     StartupList, StartupDetail)


urlpatterns = [
    url(r'^$', StartupList.as_view(), name='organizer_startup_list'),
    url(r'^create/$', StartupCreate.as_view(), 
        name='organizer_startup_create'),
    url(r'^(?P<slug>[\w\-]+)/$', StartupDetail.as_view(), 
        name='organizer_startup_detail'),
    url(r'^(?P<startup_slug>[\w\-]+)/add_article_link/$',
        NewsLinkCreate.as_view(), name='organizer_newslink_create'),
     url(r'^(?P<slug>[\w\-]+)/delete/$', StartupDelete.as_view(), 
        name='organizer_startup_delete'),
    url(r'^(?P<slug>[\w\-]+)/update/$', StartupUpdate.as_view(), 
        name='organizer_startup_update'),
    url(r'^(?P<startup_slug>[\w\-]+)/(?P<newslink_slug>[\w\-]+)/delete/$',
        NewsLinkDelete.as_view(), name='organizer_newslink_delete'),
    url(r'^(?P<startup_slug>[\w\-]+)/(?P<newslink_slug>[\w\-]+)/update/$',
        NewsLinkUpdate.as_view(), name='organizer_newslink_update'),
]
