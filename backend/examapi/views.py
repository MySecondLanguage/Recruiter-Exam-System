from django.shortcuts import render

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView
)

from rest_framework.response import Response

from rest_framework.views import APIView

from exam.models import (
    Question,
    QuestionGroup
)

from result.models import Result
from examapi.serializers import (
    QuestionSerializer,
    ResultCreateSerializer
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

class CreateResultView(CreateAPIView):
    serializer_class = ResultCreateSerializer

    def create(self, request, *args, **kwargs):
        if not request.data._mutable:
            request.data._mutable = True
        question = Question.objects.filter(id=request.data['question']).values('choices')

        # print(question, '-----------------------------------------------------')

        request.data['user'] = request.user.id
        # request.data['marks'] = request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers)


