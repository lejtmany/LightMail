from Mail.models import Email, Contact
from django.views import generic

__author__ = 'lejtman'
from django import template


register = template.Library()

@register.inclusion_tag('Mail/emails_list.html')
def emails_list():
    emails = Email.objects.exclude(sender='myemail@gmail.com')
    return {'emails':emails}

@register.inclusion_tag('Mail/contacts_list.html')
def contacts_list():
    contacts = Contact.objects.all()
    return {'contacts': contacts}