from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.signals import post_save

from account.models import Account


class Category(models.Model):
    title = models.CharField(max_length=225)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=225)

    def __str__(self):
        return self.title


class Blog(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    image = models.ImageField(upload_to='blog/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='post')
    tags = models.ManyToManyField(Tag)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Body(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_body')
    image = models.ImageField(upload_to='body')
    body = RichTextField()


class Comment(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='comment_author')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    message = models.TextField()
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    top_level_comment_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"comment of {self.author} ({self.id})"

    @property
    def get_related_comments(self):
        qs = Comment.objects.filter(top_level_comment_id=self.id).exclude(id=self.id)
        if qs:
            return qs
        return None


def comment_post_save(instance, sender, created, *args, **kwargs):
    if created:
        top_level_comment = instance
        while top_level_comment.parent_comment:
            top_level_comment = top_level_comment.parent_comment
        instance.top_level_comment_id = top_level_comment.id
        instance.save()


post_save.connect(comment_post_save, sender=Comment)
