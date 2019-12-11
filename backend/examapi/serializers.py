from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from exam.models import (
    Question,
    Choice,
    QuestionChoice
)

from result.models import Result



class ChoiceSerializer(ModelSerializer):

    class Meta:
        model = Choice
    
        fields = '__all__'

# Seriliaze profile model
class QuestionSerializer(ModelSerializer):
    choices = ChoiceSerializer(read_only=True, many=True)
    class Meta:
        model = Question
    
        fields = '__all__'

class ResultCreateSerializer(ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'