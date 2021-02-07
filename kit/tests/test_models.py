from django.test.testcases import TestCase
from model_bakery import baker
from kit.models import Category, Answer


class CategoryModelTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='Mobile Banking')

    def test_name_label(self):
        category = Category.objects.get(id=1)
        field_name = category._meta.get_field('name').verbose_name
        self.assertEqual(field_name, 'name')

    def test_name_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEqual(max_length, 250)

    def test_name_null_status(self):
        category = Category.objects.get(id=1)
        null_status = category._meta.get_field('name').null
        self.assertFalse(null_status)

    def test_name_blank_status(self):
        category = Category.objects.get(id=1)
        blank_status = category._meta.get_field('name').blank
        self.assertFalse(blank_status)

    def test_name_unique_status(self):
        category = Category.objects.get(id=1)
        unique_status = category._meta.get_field('name').unique
        self.assertTrue(unique_status)

    def test_category_str(self):
        category = Category.objects.get(id=1)
        self.assertEqual(str(category), 'Mobile Banking')


class AnswerModelTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        Answer.objects.create(answer='Yes')

    def test_answer_label(self):
        answer = Answer.objects.get(id=1)
        field_label = answer._meta.get_field('answer').verbose_name
        self.assertEqual(field_label, 'answer')

    def test_answer_max_length(self):
        answer = Answer.objects.get(id=1)
        max_length = answer._meta.get_field('answer').max_length
        self.assertEqual(max_length, 50)

    def test_answer_null_status(self):
        answer = Answer.objects.get(id=1)
        null_status = answer._meta.get_field('answer').null
        self.assertFalse(null_status)

    def test_answer_blank_status(self):
        answer = Answer.objects.get(id=1)
        blank_status = answer._meta.get_field('answer').blank
        self.assertFalse(blank_status)

    def test_answer_is_unique(self):
        answer = Answer.objects.get(id=1)
        unique_status = answer._meta.get_field('answer').unique
        self.assertTrue(unique_status)

    def test_weight_label(self):
        answer = Answer.objects.get(id=1)
        field_label = answer._meta.get_field('weight').verbose_name
        self.assertEqual(field_label, 'marks')

    def test_weight_default(self):
        answer = Answer.objects.get(id=1)
        weight_default = answer._meta.get_field('weight').default
        self.assertEqual(weight_default, 5)

    def test_answer_str(self):
        answer = Answer.objects.get(id=1)
        self.assertEqual(str(answer), 'Yes')


class QuestionModelTestClass(TestCase):

    def setUp(self):
        self.question = baker.make('kit.Question',
                                   question='Que pas?',
                                   make_m2m=True)

    def test_choices_field_many_to_many_property(self):
        choices_set = baker.prepare('kit.Answer', _quantity=5)
        question = baker.make('kit.Question', choices=choices_set)
        self.assertEqual(question.choices.count(), 5)

    def test_question_field_blank_status(self):
        blank_status = self.question._meta.get_field('question').blank
        self.assertFalse(blank_status)

    def test_question_field_null_status(self):
        null_status = self.question._meta.get_field('question').blank
        self.assertFalse(null_status)

    def test_question_field_max_length(self):
        max_length = self.question._meta.get_field('question').max_length
        self.assertEqual(max_length, 250)

    def test_choices_field_blank_status(self):
        blank_status = self.question._meta.get_field('choices').blank
        self.assertFalse(blank_status)

    def test_category_blank_status(self):
        blank_status = self.question._meta.get_field('correct_answer').blank
        self.assertFalse(blank_status)

    def test_category_null_status(self):
        null_status = self.question._meta.get_field('correct_answer').null
        self.assertTrue(null_status)

    def test_question_str(self):
        self.assertEqual(str(self.question), 'Que pas?')






