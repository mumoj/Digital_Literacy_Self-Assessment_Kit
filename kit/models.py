from django.db import models
from users.models import User


class Category(models.Model):
    """ Each question belongs to a specific category for example, desktop computers, mobile phones etc"""
    name = models.CharField(max_length=250, blank=False, null=False, unique=True)

    def __str__(self):
        return self.name


class Answer(models.Model):
    """An answer is a choice in a question. An answer can be correct or wrong"""
    answer = models.CharField(blank=False, null=False, unique=True, max_length=50)
    weight = models.IntegerField(default=5, verbose_name='marks')

    def __str__(self):
        return self.answer


class Question(models.Model):
    """This model defines a question,its choices, the category, and the correct answer."""
    question = models.CharField(max_length=250, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='questions')
    choices = models.ManyToManyField(Answer, blank=False, related_name='questions_choices')
    correct_answer = models.ForeignKey(Answer, on_delete=models.DO_NOTHING, related_name='questions_correct_answer',
                                       null=True, blank=False,
                                       )

    def __str__(self):
        return self.question
