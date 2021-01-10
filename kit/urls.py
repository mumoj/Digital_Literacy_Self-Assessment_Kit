from django.urls import path
from .views import QuestionsPageView, IndexView, ResultsView

app_name = 'kit'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('questions/<str:category_name>', QuestionsPageView.as_view(), name='questions'),
    path('results/', ResultsView.as_view(), name='results'),
    # path('questions/<int:pk>', QuestionUpdate.as_view(), name='question_update')
]
