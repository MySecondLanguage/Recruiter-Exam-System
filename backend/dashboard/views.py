from django.shortcuts import (
    render,
    HttpResponse
)

from django.db.models import Count

from exam.models import (
    Choice,
    Exam,
    Question,
    QuestionChoice,
    QuestionGroup,
    Topic
)

from result.models import Result

from account.models import (
    Profile
)

def home(request):
    return render(request, 'dashboard/index.html')

def question_pool(request):
    # topic_to_query=["css", "java"]

    qs = Topic.objects.filter(
    name__in=['css', 'java']
    ).prefetch_related('questions_by_topic')

    print(qs, '---------------------------------------------------')
    return render(request, 'dashboard/question-pool.html')



