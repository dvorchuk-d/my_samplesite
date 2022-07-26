from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.base import View, TemplateView
from django.urls import reverse_lazy
from bboard.models import MyDb, Rubrics
from bboard.forms import MyDbForm


def index(request):
    """This function renders the main paige of the app"""
    bbs = MyDb.objects.all()
    rubrics = Rubrics.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, "bboard/index.html", context)


class IndexView(TemplateView):
    """Version of index view in OOP style"""
    template_name = "bboard/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bbs'] = MyDb.objects.all()
        context['rubrics'] = Rubrics.objects.all()
        return context


def by_rubric(request, rubric_id):
    """This function renders pages with discounts of some rubric"""
    bbs = MyDb.objects.filter(rubric=rubric_id)
    rubrics = Rubrics.objects.all()
    current_rubric = Rubrics.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics,
               'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)


class MyDbCreateView(CreateView):
    """This class renders page with form to add new discount"""
    template_name = 'bboard/create.html'
    form_class = MyDbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubrics.objects.all()
        return context


class TestViewForView(View):
    """This is test class to show using of View base class"""
    http_method_names = ['get']

    def get(request, kwargs):
        return HttpResponse(f"Hello, {kwargs.META['HTTP_HOST']}")