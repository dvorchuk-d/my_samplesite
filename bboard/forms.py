from django.forms import ModelForm
from bboard.models import MyDb


class MyDbForm(ModelForm):
    """Form to add a new discount"""
    class Meta:
        model = MyDb
        fields = ('store_name', 'link', 'content', 'code',
                  'discount', 'discount_start', 'discount_end', 'rubric')
