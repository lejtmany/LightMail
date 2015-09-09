
__author__ = 'lejtman'

from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.email_detail.as_view(), name='email_detail'),
    url(r'^send_email$', views.send_email.as_view() ,name='send_email'),
]