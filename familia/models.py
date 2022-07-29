from django.db import models

class Family(models.Model):
    full_name=models.CharField(max_length=40)
    age = models.FloatField()
    genre=models.CharField(max_length=40)
    relative=models.CharField(max_length=40)
    creation_date = models.DateField(auto_now_add=True, null=True, blank=True) 