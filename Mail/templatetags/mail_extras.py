from Mail.models import Email

__author__ = 'lejtman'
from django import template


register = template.Library()

@register.inclusion_tag('Mail/inbox.html')
def inbox():
    emails = Email.objects.all()
    return {'emails':emails}

