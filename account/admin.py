from django.contrib import admin
from .models import City, Country, Company, Account


@admin.register(City)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'country')
    search_fields = ('title', )


@admin.register(Account)
class Account(admin.ModelAdmin):
    list_display = ['id', 'username']


@admin.register(Company)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', )


@admin.register(Country)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', )



