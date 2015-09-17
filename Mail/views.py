from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
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
    return render(request, 'Mail/index.html')


def send_email(request, email_id = None):
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
        return render(request, 'Mail/send_email.html', {'form': form})


def save_email_to_db(form):
    email = form.save(commit=False)
    email.date = datetime.datetime.now()
    email.sender = my_email
    email.is_deleted = False
    mail.send_mail(email.subject, email.content, email.sender, [email.receiver, ])
    form.save()


def add_contact(request):
    form = ContactForm()
    return render(request, 'Mail/add_contact.html', {'form': form})

class contacts_list(generic.ListView):
    template_name = 'Mail/contacts_list.html'
    context_object_name = 'contacts'

    def get_queryset(self):
        return Contact.objects.all()


class sent_emails(generic.ListView):
    template_name = 'Mail/sent_emails.html'
    context_object_name = 'sent_emails'

    def get_queryset(self):
        return Email.objects.filter(sender=my_email)
