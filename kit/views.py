from django.views.generic import (ListView, UpdateView)
from .models import Question
from .forms import QuestionForm


# Create your views here.
class QuestionList(ListView):
    context_object_name = 'question_list'
    model = Question
    template_name = 'questions.html'


class QuestionUpdate(UpdateView):
    context_object_name = 'question'
    model = Question
    form_class = QuestionForm
    template_name = 'question_update.html'

    def get_form_kwargs(self):
        kwargs = super(QuestionUpdate, self).get_form_kwargs()
        self.object = self.get_object()
        kwargs['pk'] = self.object.pk
        return kwargs

