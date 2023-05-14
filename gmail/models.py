from django.db import models


class Consult(models.Model):
    name = models.CharField(max_length=16)
    position = models.CharField(max_length=16, null=True)
    email = models.TextField(max_length=50, null=True)
    describe = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'Consult'
