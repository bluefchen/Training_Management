from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^lesson1data$', views.setLessonOneGrade),
    url(r'^list$', views.peoplelist),
    url(r'^person/(?P<id>[0-9]+)$', views.person),
    url(r'^person/edit/(?P<id>[0-9]+)$', views.person)
]