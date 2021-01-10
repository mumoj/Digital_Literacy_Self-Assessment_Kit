# from django import forms
# from .models import Question, Choice
#
#
# class QuestionForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         self.question_pk = kwargs.pop('pk')
#         super(QuestionForm, self).__init__(*args, **kwargs)
#         self.fields['user_answer'].queryset = Choice.objects.filter(question__pk=self.question_pk)
#     user_answer = forms.ModelChoiceField(queryset=None, widget=forms.RadioSelect)
#
#     class Meta:
#         model = Question
#         fields = ('question', 'user_answer', 'answer')
