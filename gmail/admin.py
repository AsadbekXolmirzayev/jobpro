from django.contrib import admin
from .models import Consult


@admin.register(Consult)
class Gmail(admin.ModelAdmin):
    list_display = ('id', 'name', 'position', 'email')
    search_fields = ('name', 'email')
