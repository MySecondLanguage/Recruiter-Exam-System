from django.contrib import admin

from exam.models import (
    Question,
    QuestionGroup,
    Exam,
    Choice,
    Topic,
    QuestionChoice,
    SelectedChoices
)



admin.site.register(Question)
admin.site.register(Exam)
admin.site.register(Choice)
admin.site.register(Topic)
admin.site.register(QuestionGroup)
admin.site.register(QuestionChoice)
admin.site.register(SelectedChoices)

