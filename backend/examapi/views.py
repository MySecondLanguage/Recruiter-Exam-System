from django.shortcuts import render

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView
)

from exam.models import Question
from examapi.serializers import (
    QuestionSerializer
)

class QuestionView(ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
