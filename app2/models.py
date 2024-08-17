from django.db import models

# Create your models here.
class TodoModel(models.Model):
    name=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    activity=models.CharField(max_length=100)
    complete = models.BooleanField(default="False")