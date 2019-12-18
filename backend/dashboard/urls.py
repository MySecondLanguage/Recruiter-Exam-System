from django.urls import path

from dashboard import views

urlpatterns = [
    path('', views.home, name="dashboard.home"),
    path('question-pool/', views.question_pool, name='dashboard.question_pool'),
    path('settings/', views.settings, name='dashboard.settings'),
    path('create-exam/', views.create_exam, name='dashboard.create_exam'),
    path('create-topic/', views.create_topic, name='dashboard.create_topic'),
    path('create-question_choice/', views.create_question_choice, name='dashboard.create_question_choice'),
]
