from django.shortcuts import render

from django.views.generic import TemplateView


class BookView(TemplateView):
    template_name = 'index.html'
    paginate_by = 4


class IndexTemplateView(TemplateView):
    template_name = 'contact.html'
