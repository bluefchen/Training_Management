from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index),
    url(r'^lesson1data$', views.setLessonOneGrade),
    url(r'^people$', views.peoplelist),
    url(r'^person/(?P<id>[0-9]+)$', views.person),
    url(r'^person/edit/(?P<id>[0-9]+)$', views.edit_person),
    url(r'^person/update$', views.update_person)
]