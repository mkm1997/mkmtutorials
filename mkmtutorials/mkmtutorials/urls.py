






from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings




urlpatterns = [


    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),

    url(r'^tutorial/',include('tutorial.urls')),


]


