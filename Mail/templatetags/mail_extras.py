from Mail.models import Email, Contact
from django.views import generic

__author__ = 'lejtman'
from django import template


register = template.Library()

@register.inclusion_tag('Mail/contacts_list.html')
def contacts_list():
    contacts = Contact.objects.all()
    return {'contacts': contacts}