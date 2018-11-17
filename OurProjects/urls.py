from django.conf.urls import url

from Gallery.urls import urlpatterns
from . import views

urlpatterns = [
    url(r'^$', views.ourprojects, name='ourprojects'),
]