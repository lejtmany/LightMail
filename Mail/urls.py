__author__ = 'lejtman'

from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.email_detail.as_view(), name='email_detail'),
    url(r'^compose_email$', views.compose_email, name='compose_email'),
    url(r'^compose_email/(?P<email_id>[0-9]+)/$', views.compose_email, name='compose_email'),
    url(r'^sent_emails$', views.sent_emails.as_view(), name='sent_emails'),
    url(r'^contacts$', views.contacts_list.as_view(), name='contacts'),
    url(r'^add_contact$', views.add_contact, name='add_contact'),
    url(r'^contact_details/(?P<pk>[0-9]+)/$', views.contact_details.as_view(), name='contact_details'),
    url(r'^api/get_contacts/$', views.get_contacts, name='get_contacts')
]
