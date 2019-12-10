from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from exam.models import (
    Question,
    Choice,
    QuestionChoice
)



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