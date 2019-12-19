from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from exam.models import (
    Question,
    Choice,
    QuestionChoice,
    Exam
)

from result.models import (
    ResultSummery,
    Result
)

from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]



class ChoiceSerializer(ModelSerializer):

    class Meta:
        model = Choice
    
        fields = '__all__'

# Seriliaze profile model
class QuestionSerializer(ModelSerializer):
    choices = ChoiceSerializer(read_only=True, many=True)
    total_second = serializers.SerializerMethodField()
    class Meta:
        model = Question
    
        fields = '__all__'


    def get_total_second(self, obj):
        exam = Exam.objects.filter(
            is_published=True
        ).first()

        if str(exam.total_duration) == '0:00:00':
            total_duration = str(obj.total_duration)
            h, m, s = total_duration.split(':')
            return int(h) * 3600 + int(m) * 60 + int(s)
        else:
            total_duration = str(exam.total_duration)
            h, m, s = total_duration.split(':')

            question = Question.objects.filter(
                exam__id=exam.id
            ).count()

            total_second = int(h) * 3600 + int(m) * 60 + int(s)
            return int(total_second) // int(question)

    

class ResultCreateSerializer(ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'


class ResultSummerySerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = ResultSummery
        fields = '__all__'