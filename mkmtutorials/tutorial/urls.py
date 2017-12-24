from django.conf.urls import url
from . import views




urlpatterns=[


        url(r'^tute/',views.MKMTUTE.as_view(),name='tute'),
        url(r'^home/',views.home.as_view(),name='home'),
        url(r'^sign/',views.signup,name='sign'),
        url(r'^new/',views.check.as_view(),name='new'),
        url(r'^cplus/',views.cplusplus.as_view(),name='cplus'),
        url(r'^js/',views.javascript.as_view(),name='js'),
        url(r'^java/',views.java.as_view(),name='java'),
        url(r'^python/',views.python.as_view(),name='python'),
        url(r'^about/',views.about.as_view(),name='about'),
        url(r'^compile/',views.compile.as_view(),name='compile'),
        url(r'^search/?$', views.your_view, name='search'),
        url(r'^contact/$',views.contactus,name='contact'),



]