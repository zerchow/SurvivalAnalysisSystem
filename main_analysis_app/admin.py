from django.contrib import admin
from main_analysis_app.models import RunoobTest
from main_analysis_app.models import Contact
from main_analysis_app.models import Tag


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email')

# Register your models here.
admin.site.register(model_or_iterable=Contact, admin_class=ContactAdmin)
admin.site.register(model_or_iterable=[RunoobTest, Tag])
