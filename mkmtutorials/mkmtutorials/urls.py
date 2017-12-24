






from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from tutorial import views



urlpatterns = [


    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),

    url(r'^tutorial/',include('tutorial.urls')),


]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns=[

        url(r'^__debug__',include(debug_toolbar.urls)),
    ]+ urlpatterns