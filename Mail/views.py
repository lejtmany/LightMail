from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Email, Contact
from .forms import EmailForm
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
            email = form.save(commit=False)
            email.date = datetime.datetime.now()
            email.sender = my_email
            email.is_deleted = False
            mail.send_mail(email.subject, email.content, email.sender, [email.receiver,])
            form.save()
            return HttpResponseRedirect(reverse('mail:index'))
    else:
        respond_to = get_object_or_404(Email, pk=email_id).sender
        form = EmailForm(initial={'receiver':respond_to})
        return render(request, 'Mail/send_email.html', {'form': form})


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
