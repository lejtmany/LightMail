import json
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import generic
from pip.commands import search
from .models import Email, Contact
from .forms import EmailForm, ContactForm
from django.core.urlresolvers import reverse
import datetime
from django.core import mail

my_email = 'myemail@gmail.com'


class email_detail(generic.DetailView):
    model = Email
    template_name = 'Mail/email_detail.html'


def IndexView(request):
     emails = Email.objects.exclude(sender='myemail@gmail.com')
     searchParams = request.GET.get('searchParams')
     if searchParams is not None:
         emails = emails.filter(content__icontains=searchParams) | emails.filter(subject__icontains=searchParams) | emails.filter(sender__icontains=searchParams)
     return render(request, 'Mail/index.html', {'emails':emails, 'searchParams':searchParams})


def compose_email(request, email_id = None):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if (form.is_valid()):
            save_email_to_db(form)
            return HttpResponseRedirect(reverse('mail:index'))
    else:
        try:
            respond_to = Email.objects.get(pk=email_id).sender
            form = EmailForm(initial={'receiver':respond_to})
        except Email.DoesNotExist:
            form = EmailForm()
        return render(request, 'Mail/compose_email.html', {'form': form})


def save_email_to_db(form):
    email = form.save(commit=False)
    email.date = datetime.datetime.now()
    email.sender = my_email
    email.is_deleted = False
    mail.send_mail(email.subject, email.content, email.sender, [email.receiver, ])
    form.save()


def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if (form.is_valid()):
            form.save()
            return HttpResponseRedirect(reverse('mail:contacts'))
    else:
        form = ContactForm()
        return render(request, 'Mail/add_contact.html', {'form': form})

class contacts_list(generic.ListView):
    template_name = 'Mail/contacts_list.html'
    context_object_name = 'contacts'

    def get_context_data(self, **kwargs):
        context = super(contacts_list, self).get_context_data(**kwargs)
        context['searchParams'] = self.request.GET.get('searchParams')
        return context

    def get_queryset(self):
        searchParams = self.request.GET.get('searchParams')
        if searchParams is None:
            return Contact.objects.all()
        else:
            return Contact.objects.filter(first_name__icontains=searchParams) | Contact.objects.filter(last_name__icontains=searchParams) | Contact.objects.filter(email__icontains=searchParams)


class sent_emails(generic.ListView):
    template_name = 'Mail/sent_emails.html'
    context_object_name = 'sent_emails'

    def get_queryset(self):
        return Email.objects.filter(sender=my_email)

class contact_details(generic.DetailView):
    model=Contact
    template_name = 'Mail/contact_details.html'

def get_contacts(request):
    searchParams = request.GET.get('term','')
    contacts = Contact.objects.filter(first_name__icontains=searchParams) | Contact.objects.filter(last_name__icontains=searchParams) | Contact.objects.filter(email__icontains=searchParams)
    names = []
    for contact in contacts:
        full_name = contact.first_name + " " + contact.last_name
        name_values = {}
        name_values['id'] = contact.id
        name_values['label'] = full_name
        name_values['value'] = contact.email
        names.append(name_values)
    data = json.dumps(names)
    return HttpResponse(data, 'application/json')