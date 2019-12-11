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

from result.models import Result
from examapi.serializers import (
    QuestionSerializer
)

class QuestionListView(RetrieveAPIView):
    serializer_class = QuestionSerializer
    
    def get_object(self):
        result = Result.objects.filter(
            user=self.request.user
        ).values(
            'question__id'
        )

        queryset = Question.objects.filter(
            exam=self.request.current_exam
        ).exclude(
            result__question__id__in=[result]
        ).first()
        return queryset


