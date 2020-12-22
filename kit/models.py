from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Choice(models.Model):
    choice = models.CharField(unique=True, max_length=50, primary_key=True)

    def __str__(self):
        return self.choice


class Question(models.Model):
    question = models.CharField(max_length=250)
    choices = models.ManyToManyField(Choice)
    answer = models.CharField(max_length=50, null=False)
    user_answer = models.CharField(max_length=50, null=True, blank=True)

    def get_absolute_url(self):
        return reverse("kit:question_update", kwargs={'pk': self.pk})

    def __str__(self):
        return self.question


