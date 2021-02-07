from pprint import pprint
from model_bakery import baker
from django.test import TestCase
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from kit.models import (Category, Question, Answer)
from kit.views import (calculate_marks_per_category, calculate_total_marks_scored,
                       calculate_test_total_marks)


class TestIndexView(TestCase):
    def test_template_used(self):
        self.assertTemplateUsed('kit/questions.html')


class TestQuestionsPageView(TestCase):

    def setUp(self) -> None:
        self.question = get_object_or_404(Question, pk=1)
        self.answer = Answer.objects.get(id=1)

    def test_template_used(self):
        self.assertTemplateUsed('kit/questions.html')

    def test_get_function(self):
        response = self.client.get(reverse('kit:questions'))
        self.assertContains(response, 'name')
        self.assertEqual(response.status_code, 200)

    def test_post_function(self):
        data = {
            'csrfmiddlewaretoken': ['d1bUCjPMq7zvQ2zihCPayBw9lsSfWdp4ZK9oqRBW107nA2jzlpCbEiuePOCzsUtM'],
            '1': ['3'],
        }
        response = self.client.post(reverse('kit:questions'))
        pass


class TestCalculateMarks(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.categories = baker.make('kit.Category', _quantity=3)
        cls.answers = baker.make('kit.Answer', _quantity=5)
        cls.questions = baker.make('kit.Question', _quantity=2, make_m2m=True)

    def test_calculate_marks_per_category(self):
        data = {'1': ['1'], '2': ['']}
        pass

    def test_calculate_marks_scored(self):
        pass

    def test_calculate_total_marks_in_the_test(self):
        pass
