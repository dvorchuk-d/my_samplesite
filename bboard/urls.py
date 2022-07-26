from ast import In
from django.urls import path
from bboard.views import index, by_rubric, MyDbCreateView, TestViewForView, IndexView


urlpatterns = [
    path('add/', MyDbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', IndexView.as_view(), name='index'),
    path('test_for_view', TestViewForView.as_view(), name='test')
]
