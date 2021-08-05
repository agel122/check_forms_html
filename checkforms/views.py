from django.shortcuts import render
from django.views.generic import TemplateView


class MyFormView(TemplateView):
    template_name = "myformpage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        context['mydata'] = "it's my additional data:"

        return context


