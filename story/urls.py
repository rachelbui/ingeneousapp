from django.conf.urls import include, url
from . import views

#pk is primary key that refers back to view

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^story/(?P<pk>[0-9]+)/$', views.post_detail),
]
