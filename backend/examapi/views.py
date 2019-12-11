from django.shortcuts import render

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView
)

from rest_framework.response import Response

from rest_framework.views import APIView

from exam.models import (
    Question,
    QuestionGroup
)
from examapi.serializers import (
    QuestionSerializer
)

class QuestionListView(RetrieveAPIView):
    serializer_class = QuestionSerializer
    
    def get_object(self):
        queryset = Question.objects.filter(
            exam=self.request.current_exam
        ).first()
        return queryset


