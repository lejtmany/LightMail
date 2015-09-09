from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from .models import Email
from django import template


class IndexView(generic.ListView):
    template_name = 'Mail/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Email.objects.all()

class email_detail(generic.DetailView):
    model = Email
    template_name = 'Mail/email_detail.html'

class send_email(CreateView):
    template_name = 'Mail/send_email.html'
    model = Email
    fields = ['sender', 'subject', 'content']


