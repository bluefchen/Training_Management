from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^password$', views.password),
    url(r'^reset/password$', views.reset_password),
    url(r'^people$', views.peoplelist),
    url(r'^person/(?P<id>[0-9]+)$', views.person),
    url(r'^person/edit/(?P<id>[0-9]+)$', views.edit_person),
    url(r'^person/update$', views.update_person),
    url(r'^person/delete/(?P<id>[0-9]+)$', views.delete_person),
    url(r'^analysis/(?P<lesson>[a-z]+[0-9]+)/(?P<id>[0-9]+)$', views.lesson_analysis),
]