from bboard.models import MyDb, Rubrics
from django.shortcuts import render
from django.views.generic.edit import CreateView
from bboard.forms import MyDbForm
from django.urls import reverse_lazy


def index(request):
    bbs = MyDb.objects.all()
    rubrics = Rubrics.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, "bboard/index.html", context)


def by_rubric(request, rubric_id):
    bbs = MyDb.objects.filter(rubric=rubric_id)
    rubrics = Rubrics.objects.all()
    current_rubric = Rubrics.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)


class MyDbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = MyDbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubrics.objects.all()
        return context
