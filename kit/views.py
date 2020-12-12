from django.shortcuts import render
from django.views.generic import (DetailView, TemplateView, ListView)
from .models import Question
from .forms import QuestionForm


# Create your views here.
class QuestionView(TemplateView):
    model = Question
    form_class = QuestionForm
    template_name = 'kit/questions.html'

    def get_form_kwargs(self):
        pass


