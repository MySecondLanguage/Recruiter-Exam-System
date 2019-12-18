from django import forms

from exam.models import (
    Question,
    Choice
)

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'title'
        ]

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'title',
            'total_duration'
        ]

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = [
            'choice_text',
            'is_right_choice'
        ]