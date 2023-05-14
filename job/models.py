from django.db import models
from account.models import Account, City, Company, Country


class Category(models.Model):
    title = models.CharField(max_length=225)

    def __str__(self):
        return self.title


class Type(models.Model):
    title = models.CharField(max_length=225)

    def __str__(self):
        return self.title


class Jobs(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    working_time = models.IntegerField(null=True, blank=True)
    job_type = models.ManyToManyField(Type, null=True, blank=True)
    position = models.CharField(max_length=225)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    location = models.ForeignKey(City, on_delete=models.CASCADE)
    price = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=225, null=True, blank=True)
    is_active = models.BooleanField(default=True)


class ApplyJob(models.Model):
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    name = models.ForeignKey(Account, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    created_date = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.job


class Like(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    jobs = models.ForeignKey(Jobs, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.author
