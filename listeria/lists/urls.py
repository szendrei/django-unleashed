from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$', views.list_list, name="lists_list_list"),
    url(r'^create/$', views.ListCreate.as_view(), name="lists_list_create"),
   url(r'^(?P<slug>[\w\-]+)/$', views.list_detail, name="lists_list_detail"),
]
