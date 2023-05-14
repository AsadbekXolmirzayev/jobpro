from django.contrib import admin
from .models import Contact, Subscribe


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_date')
    search_fields = ('name', 'email')
    date_hierarchy = 'created_date'


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    search_fields = ('email', )

