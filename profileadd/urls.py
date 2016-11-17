from django.conf.urls import include, url
from . import views

urlpatterns = [
    # url(r'^', include('profileadd.urls')),
    url(r'^userprofile/$', views.profile),
]
