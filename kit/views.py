from django.views.generic import TemplateView
from django.views import View
from .models import Question, Category, Answer
from django.shortcuts import render, redirect
from django.contrib import messages


class IndexView(TemplateView):
    template_name = 'index.html'


class QuestionsPageView(View):
    template = 'questions.html'

    def get(self, request, *args, **kwargs):
        context = {
            'categories': Category.objects.all()
        }
        return render(request, self.template, context)

    def post(self, request, *args, **kwargs):
        data = dict(request.POST.copy())
        data.pop('csrfmiddlewaretoken')

        request.session['marks_per_category'] = calculate_marks_per_category(data=data)

        return redirect('kit:results')


class ResultsView(View):
    template = 'results.html'

    def get(self, request):
        marks_per_category = request.session.get('marks_per_category')

        context = {
            'marks_per_category': marks_per_category,
            'total_marks_scored': calculate_total_marks_scored(marks_per_category),
            'test_total_marks': calculate_test_total_marks(),
        }

        return render(request, self.template, context)


def calculate_marks_per_category(data) -> dict:
    """Calculate the marks per category."""

    categories = Category.objects.all()
    marks_per_category = {category.name: 0 for category in categories}

    for key in data:
        question = Question.objects.get(id=int(key))
        user_answer = Answer.objects.get(id=int(data[key][0]))

        if user_answer.answer == str(question.correct_answer):
            marks_per_category[str(question.category)] += user_answer.weight
        else:
            marks_per_category[str(question.category)] += 0

    return marks_per_category


def calculate_total_marks_scored(marks_per_category: dict) -> int:
    """Calculate the total marks the user scored."""

    total_marks = 0

    for marks in marks_per_category.values():
        total_marks += marks
    return total_marks


def calculate_test_total_marks() -> int:
    """Calculate the total marks for the test."""

    questions = Question.objects.all()
    total_marks = 0

    for question in questions:
        total_marks += int(question.correct_answer.weight)
    return total_marks
