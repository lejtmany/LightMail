__author__ = 'lejtman'

from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.email_detail.as_view(), name='email_detail'),
    url(r'^send_email$', views.send_email, name='send_email'),
    url(r'^send_email/(?P<email_id>[0-9]+)/$', views.send_email, name='send_email'),
    url(r'^sent_emails$', views.sent_emails.as_view(), name='sent_emails'),
    url(r'^contacts$', views.contacts_list.as_view(), name='contacts'),
]
