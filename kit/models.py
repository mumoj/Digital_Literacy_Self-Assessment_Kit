from django.db import models
from users.models import User


class Category(models.Model):
    # Each question belongs to a specific category for example, computers, phones etc
    name = models.CharField(max_length=250, blank=False, null=False, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

 
class Answer(models.Model):
    # An answer is a choice in a question. Yes No answers are not unique. An answer can be correct or wrong
    answer = models.CharField(blank=False, null=False, unique=False, max_length=250)  # No need to specify that it is a primary key. Answers can be long
    weight = models.IntegerField(default=5, verbose_name='marks')

    def __str__(self):
        return self.answer


class Question(models.Model):
    ANSWER_TYPE_CHOICES = (
        ('RADIO', 'RADIO'),
        ('SELECT', 'SELECT')
    )
    question = models.CharField(max_length=250, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='questions')
    choices = models.ManyToManyField(Answer, blank=False, related_name='questions_choices')
    # Not all questions need a correct answer, for example, have you ever used a mobile phone?
    # correct_answers = models.ManyToManyField(Answer, blank=True, related_name='questions_correct_answers')
    answer_type = models.CharField(max_length=10, choices=ANSWER_TYPE_CHOICES, blank=False, null=False, default='RADIO')

    def __str__(self):
        return self.question


class UserResponse(models.Model):
    user = models.ForeignKey(User, related_name='responses', on_delete=models.PROTECT)
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, blank=True, null=True)
    user_answers = models.ManyToManyField(Answer, related_name='user_answers')


