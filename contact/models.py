from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField(max_length=225)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Subscribe(models.Model):
    email = models.EmailField(max_length=225, db_index=True)

    def __str__(self):
        return self.email
