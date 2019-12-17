from django.urls import path, re_path
from account import views

urlpatterns = [
    path('', views.home, name="account.home"),
    path('report/', views.report, name='account.report'),
]
