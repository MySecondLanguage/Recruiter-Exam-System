from django.shortcuts import render

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView
)

from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView

from exam.models import (
    Question,
    QuestionGroup,
    Choice,
    Exam
)

from result.models import (
    ResultSummery,
    Result
)
from examapi.serializers import (
    QuestionSerializer,
    ResultCreateSerializer,
    ResultSummerySerializer
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
        )

        # Update result summery if not question remained to answer
        if not queryset.exists():
            summery = ResultSummery.objects.get(exam__id=self.request.current_exam.id)
            summery.is_exam_completed = True
            summery.save()
        return queryset.first()



class CreateResult(CreateAPIView):
    serializer_class = ResultCreateSerializer
    """
        POPULATE result.models.Results IF EXAMINEE ANSWER QUESTION OR NOT
        IF EXAMINEE ANSWER IS WRONG, MARKS FIELDS VALUE WILL BE 0,
        IF EXAMINEE ANSWER IS RIGHT, MARKS FIELDS VALUE WILL BE 1
    """

    def create(self, request, *args, **kwargs):
        answered_choice = Choice.objects.filter(
            id__in=request.data['answer']
        ).values(
            'id',
            'is_right_choice'
        )

        get_false = [choice_false for choice_false in answered_choice if not choice_false['is_right_choice']]
        
        if not get_false:
            marks = 1
        else:
            marks = 0
    
        result_data = {
            'question': request.data['question'],
            'marks': marks,
            'user': request.user.id,
            'elapsed': request.data['elapsed']
        }
        
        serializer = self.get_serializer(data=result_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ResultSummeryView(ListAPIView):
    serializer_class = ResultSummerySerializer

    def get_queryset(self):
    
        queryset = ResultSummery.objects.filter(
            exam__id=self.request.current_exam.id
        ).order_by(
            '-total_marks',
            'total_elapsed_second'
        )
        
        return queryset
