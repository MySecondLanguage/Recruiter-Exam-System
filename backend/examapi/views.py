from django.shortcuts import render

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView
)

from exam.models import Question
from examapi.serializers import (
    QuestionSerializer
)

class QuestionListView(ListAPIView):
    serializer_class = QuestionSerializer
    
    def get_queryset(self):
        queryset = Question.objects.filter(
            id=1
        ).first()
        return queryset
