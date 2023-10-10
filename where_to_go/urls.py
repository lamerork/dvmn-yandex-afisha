from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.urls import path, re_path, include
from .views import show_index, show_detail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_index),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path('places/<int:id>', show_detail, name='place_detail'),
    path('tinymce/', include('tinymce.urls')),
]
