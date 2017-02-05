from django.conf.urls import url

from .views import (category_list, category_detail, 
                    CategoryCreate, CategoryUpdate, CategoryDelete)

urlpatterns = [
    url(r'^$', category_list, name='categories_category_list'),
    url(r'^create/$', CategoryCreate.as_view(), 
        name='categories_category_create'),
    url(r'^(?P<slug>[\w\-]+)/$', category_detail, 
        name='categories_category_detail'),
    url(r'^(?P<slug>[\w\-]+)/update/$', CategoryUpdate.as_view(),
        name='categories_category_update'),
        url(r'^(?P<slug>[\w\-]+)/delete/$', CategoryDelete.as_view(),
        name='categories_category_delete'),
]
