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
    total_duration = serializers.SerializerMethodField()
    class Meta:
        model = Question
    
        fields = '__all__'


    def get_total_duration(self, obj):
        total_duration = str(obj.total_duration)
        h, m, s = total_duration.split(':')
        return int(h) * 3600 + int(m) * 60 + int(s)

    

class ResultCreateSerializer(ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'