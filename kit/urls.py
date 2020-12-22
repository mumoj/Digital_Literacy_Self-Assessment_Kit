from django.urls import path
from .views import QuestionList, QuestionUpdate

app_name = 'kit'
urlpatterns = [
    path('questions/', QuestionList.as_view(), name='question_list'),
    path('questions/<int:pk>', QuestionUpdate.as_view(), name='question_update')
]
