from django.contrib import admin
from .models import Category, Type, Jobs, ApplyJob, Like


@admin.register(Jobs)
class JobsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'working_time', 'category', 'company', 'location', 'price',
                    'description', 'is_active')
    search_fields = ('title', 'company', 'category', 'price')


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', )


@admin.register(ApplyJob)
class ApplyJob(admin.ModelAdmin):
    list_display = ('id', 'job', 'name', 'resume')
    search_fields = ('job', 'name')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'jobs', 'author')
    search_fields = ('jobs', 'author')
