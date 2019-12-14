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
    context = {}
    topic = Topic.objects.all()
    context['topics'] = topic

    if request.GET:
        topic_to_query=list(request.GET.keys())
        questions_by_topic = Topic.objects.filter(
        name__in=topic_to_query
        ).prefetch_related(
            'questions_by_topic'
        )

        # """
        # WE SHOULD CONSTRUCT RESULT LIKE THIS BELOW IF YOU WANT TO QUERY IN TEMPLATE LABEL
        # {% for question in topic.questions_by_topic.all %}
        # """
        # result = {
        #     t.name: [{'id': q.id, 'title': q.title} for q in t.questions_by_topic.all()]
        #     for t in questions_by_topic
        # }

        context['topic_question'] = questions_by_topic

    if request.POST:
        q_id = list(request.POST.keys())
        del q_id[0]

        for q in q_id:
            QuestionGroup.objects.create(
                exam=request.current_exam,
                question=Question.objects.get(id=q)
            )
        
    return render(request, 'dashboard/question-pool.html', context)



