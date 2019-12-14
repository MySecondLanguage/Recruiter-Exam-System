from django.urls import path

from dashboard import views

urlpatterns = [
    path('', views.home, name="dashboard.home"),
    path('question-pool', views.question_pool, name='dashboard.question_pool')
]
