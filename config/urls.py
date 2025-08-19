"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

from .errors import (
    PageNotFoundView,
    custom_400_view,
    custom_401_view,
    custom_403_view,
    custom_500_view,
)

from django.conf.urls import (
    handler404,
    handler400,
    handler403,
    handler500,
)

from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('uzmovie/', admin.site.urls),

    path('i18n/', include('django.conf.urls.i18n')),

    # libs urls
    path('ckeditor/', include('ckeditor_uploader.urls')),

    re_path(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,
            {'document_root': settings.STATIC_ROOT}),
]

urlpatterns += i18n_patterns(
    path('unauthorized/', custom_401_view, name='unauthorized'),
    # Translated URLs
    # local urls
    #
    path(
        '',
        include('apps.contact.urls')
    ),
    path(
        '',
        include('apps.users.urls')
    ),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

page_not_found_view = PageNotFoundView.as_view()

handler400 = custom_400_view
handler403 = custom_403_view
handler404 = page_not_found_view
handler500 = custom_500_view
