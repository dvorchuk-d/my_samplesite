from django.contrib import admin
from bboard.models import MyDb
from bboard.models import Rubrics


class MyDbAdmin(admin.ModelAdmin):
    """Model view for administrative mode of app"""
    list_display = ('store_name', 'content', 'discount',
                    'discount_start', 'discount_end', 'rubric')
    list_display_links = ('store_name',)
    search_fields = ('discount', 'store_name')


admin.site.register(MyDb, MyDbAdmin)

admin.site.register(Rubrics)
