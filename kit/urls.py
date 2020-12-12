from django.urls import path
from .views import QuestionView

app_name = 'kit'
urlpatterns = [
    path('questions/', QuestionView.as_view(), name='questions')
]

