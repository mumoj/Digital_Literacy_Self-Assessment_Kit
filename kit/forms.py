from django import forms
from.models import Question, Choice


class QuestionForm(forms.ModelForm):
    choices = forms.ModelChoiceField(queryset=Choice.objects.all(), widget=forms.RadioSelect)

    class Meta:
        model = Question
        fields = ('question', 'choices')


