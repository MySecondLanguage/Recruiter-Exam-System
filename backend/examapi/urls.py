from django.urls import path
from examapi import views

urlpatterns = [
    path('question-list/', views.QuestionListView.as_view(), name='exam')
]
