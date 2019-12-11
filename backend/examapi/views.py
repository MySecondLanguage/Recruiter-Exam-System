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
    QuestionGroup,
    Choice
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


class CreateResult(APIView):
    """
        POPULATE result.models.Results IF EXAMINEE A QUESTION OR NOT
        IF EXAMINEE ANSWER IS WRONG, MARKS FIELDS VALUE WILL BE 0,
        IF EXAMINEE ANSWER IS RIGHT, MARKS FIELDS VALUE WILL BE 1
    """

    def get(self, request, format=None):
        # GET THE QUESTION THAT USER TRIED TO INTERACT
        # question = Question.objects.filter(id=request.GET['question_id']).values('choices', 'id')
        
        # GET THE CHOICE FIELDS EXAMINEE SELECTED
        answered_choice = Choice.objects.filter(
            id__in=[request.GET['choice_1']]
        ).values(
            'id',
            'is_right_choice'
        )

        # # GET ALL THE CHOICES WITH QUESTION THAT EXAMINEE TRIED INTERACT
        # choices = Choice.objects.filter(id__in=[choice['choices'] for choice in question]).values('id', 'is_right_choice')

        # """
        #  FILTER ALL THE CHOICES WITH THOSE CHOICES THAT EXAMINEE
        # """
        # filter_choice = [choice for choice in choices if choice in answered_choice]

        get_false = [choice_false for choice_false in answered_choice if not choice_false['is_right_choice']]
        

        if not get_false:
            marks = 1
        else:
            marks = 0
        
       
        


        return Response(request.GET)