from django.views.generic import (ListView, UpdateView)
from django.views import View
from .models import Question, Category, Answer, UserResponse
from django.shortcuts import render, redirect
from django.contrib import messages
# from .forms import QuestionForm


class IndexView(View):
    template = 'kit/index.html'

    def get(self, request):
        context = {
            'categories': Category.objects.all()
        }
        return render(request, template_name=self.template, context=context)


class QuestionsPageView(View):
    template = 'kit/questions.html'

    def get(self, request, *args, **kwargs):
        category = self.kwargs.get('category_name', '')
        context = {
            'current_category': category,
            'questions': Question.objects.filter(category__name=category)
        }
        return render(request, self.template, context)

    def post(self, request, *args, **kwargs):
        data = dict(request.POST.copy())
        data.pop('csrfmiddlewaretoken')

        user_responses = []

        for key in data:
            question = Question.objects.get(id=int(key))

            user_answers = []
            for ans_id in data[key]:
                answer = Answer.objects.get(id=int(ans_id))
                user_answers.append(answer)

            user_responses.append({'question': question, 'user_answers': user_answers})

        return redirect('/results?score={}'.format(calculate_score(user_responses)))


class ResultsView(View):
    template = 'kit/results.html'

    def get(self, request):
        context = {}
        score = request.GET.get('score', None)

        if score is not None:
            context['score'] = score

            return render(request, self.template, context)

        return redirect('/')


def calculate_score(user_responses):
    scored_marks = 0

    for resp in user_responses:
        for answer in resp['user_answers']:
            scored_marks += answer.weight or 0

    return scored_marks
