from django.conf.urls import url

from .views import (PostArchiveMonth, PostArchiveYear, PostCreate, 
                    PostDelete, PostList, PostUpdate, PostDetail)

urlpatterns = [
    url(r'^$', PostList.as_view(), name='blog_post_list'),
    url(r'^create/$', PostCreate.as_view(), name='blog_post_create'),
    url(r'^(?P<year>\d{4})/$', PostArchiveYear.as_view(),
        name='blog_post_archive_year'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$', PostArchiveMonth.as_view(),
        name='blog_post_archive_month'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[\w\-]+)/$', 
        PostDetail.as_view(), name='blog_post_detail'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[\w\-]+)/update/$',
        PostUpdate.as_view(), name='blog_post_update'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[\w\-]+)/delete/$',
        PostDelete.as_view(), name='blog_post_delete'),
]
