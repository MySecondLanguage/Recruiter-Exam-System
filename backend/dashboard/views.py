from django.shortcuts import (
    render,
    HttpResponse
)

from exam.models import (
    Choice,
    Exam,
    Question,
    QuestionChoice,
    QuestionGroup
)

from result.models import Result

from account.models import (
    Profile
)

def home(request):
    return HttpResponse('hello world')

