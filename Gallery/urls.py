from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.gallery, name='gallery'),

    # Gallery/Some id
    #url(r'^(?P<image_id>[0-9]+)/$', views.detail, name='detail'),

    # Gallery/Some id/fav/
    #url(r'^(?P<image_id>[0-9]+)/fav/$', views.detail, name='fav'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
