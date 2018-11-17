from django.contrib import admin
from django.conf.urls import include, url


app_name = 'Gallery'


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Gallery/', include('Gallery.urls')),
    url(r'^Home/', include('Home.urls')),
    url(r'^OurProjects/', include('OurProjects.urls')),

]
