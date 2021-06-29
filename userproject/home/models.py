from io import DEFAULT_BUFFER_SIZE
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.fields import BooleanField, CharField

# Create your models here.




class Project(models.Model):
    track = models.CharField(max_length=100)


    def __str__(self):
        return self.track


    class UserTask(models.Model):

        Task_title = models.ForeignKey(User, on_delete=models.CASCADE)
        start_time = models.CharField(max_length=100)
        end_task = models.CharField(max_length=100)
        status = models.BooleanField(default=True)

    