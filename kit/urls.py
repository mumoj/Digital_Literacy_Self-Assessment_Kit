from django.urls import path
from .views import QuestionsPageView, IndexView, ResultsView

app_name = 'kit'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('questions/', QuestionsPageView.as_view(), name='questions'),
    path('results/', ResultsView.as_view(), name='results'),
]
