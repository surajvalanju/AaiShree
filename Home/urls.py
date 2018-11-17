from django.conf.urls import url

from Gallery.urls import urlpatterns
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^ContactUs/', views.contactus, name='contactus'),
    url(r'^AboutUs/', views.aboutus, name='aboutus'),

]