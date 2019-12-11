from django.urls import path
from examapi import views

urlpatterns = [
    path('question-list/', views.QuestionListView.as_view(), name='examapi.exam_list'),
    path('result-create/', views.CreateResultView.as_view(), name='examapi.create_result')
]
