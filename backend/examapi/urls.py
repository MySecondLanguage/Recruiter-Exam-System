from django.urls import path, re_path
from examapi import views

urlpatterns = [
    path('question-list/', views.QuestionListView.as_view(), name='examapi.exam_list'),
    path('create-result/', views.CreateResult.as_view(), name='examapi.result_create'),
    path('result-summery/', views.ResultSummeryView.as_view(), name='examapi.result_summery'),
]
