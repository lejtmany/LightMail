from django.shortcuts import render
from django.views import generic
from .models import Email
from django import template


class IndexView(generic.ListView):
    template_name = 'Mail/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Email.objects.all()


