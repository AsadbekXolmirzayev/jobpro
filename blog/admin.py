from django.contrib import admin
from .models import Blog, Category, Tag, Body, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', )


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'image', 'category', 'description', 'created_date')
    search_fields = ('author', 'category')


@admin.register(Body)
class BodyAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'image', 'body')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'parent_comment', 'top_level_comment_id', 'created_date')
    search_fields = ('author__first_name', 'author__last_name', 'author__username', 'post__title', 'top_level_comment_id')
    date_hierarchy = 'created_date'


