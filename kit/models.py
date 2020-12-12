from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Choice(models.Model):
    choice = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.choice


class Question(models.Model):
    question = models.CharField(max_length=250)
    choices = models.ManyToManyField(Choice, related_name='choices')
    answer = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='answer')

    def __str__(self):
        return self.question


