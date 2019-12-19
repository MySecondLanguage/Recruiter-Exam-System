from django.shortcuts import (
    render,
    HttpResponse,
    redirect
)

from django.db.models import Count

from datetime import timedelta

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
    if request.user.is_superuser:
        return render(request, 'dashboard/index.html')
    else:
        return HttpResponse('You are not allowed to access to this page')

def question_pool(request):
    if request.user.is_superuser:
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
    else:
        HttpResponse('You are not allowed to acccess to this page')


def settings(request):
    exams = Exam.objects.all()
    context = {'exams': exams}
    if request.method == 'POST':
        for exam in exams:
            exam.is_published = False
            exam.save()
        
        current_exam_will_be = Exam.objects.get(id=str(request.POST['exam']))
        current_exam_will_be.is_published = True
        current_exam_will_be.save()

    return render(request, 'dashboard/settings.html', context)


def create_exam(request):
    if request.method == 'GET':
        pass
    else:
        if request.POST['duration']:
            duration = timedelta( days=0, hours=0, minutes=0, seconds=int(request.POST['duration']) )
        else:
            duration = timedelta( days=0, hours=0, minutes=0, seconds=0 )
        print(request.POST['exam'])
        exam = Exam.objects.create(
            name=request.POST['exam'],
            total_duration=duration
        )
        all_exam = Exam.objects.all().exclude(id=exam.id)
        for i in all_exam:
            i.is_published = False
            i.save()
        return redirect('dashboard.question_pool')
    return render(request, 'dashboard/create_exam.html')

def create_topic(request):
    if request.method == 'GET':
        pass
    else:
        Topic.objects.create(
            name=request.POST['name'],
        )
        
        return redirect('dashboard.create_question_choice')
    return render(request, 'dashboard/create_topic.html')


def create_question_choice(request):
    context = {}
    topic = Topic.objects.all()
    context['topics'] = topic
    if request.method == 'POST':
        duration = timedelta( days=0, hours=0, minutes=0, seconds=int(request.POST['total_duration']) )
        question = Question.objects.create(
            title=request.POST['title'],
            total_duration=duration,
            topic=Topic.objects.get(id=str(request.POST['topic']))
        )

        form_list = []

        if 'choice_text_1' in request.POST:
            choice_dict = {'choice_text': request.POST['choice_text_1']}
            if 'is_right_choice_1' in request.POST:
                choice_dict['is_right_choice'] = True
            else:
                choice_dict['is_right_choice'] = False
        form_list.append(choice_dict)

        if 'choice_text_2' in request.POST:
            choice_dict = {'choice_text': request.POST['choice_text_2']}
            if 'is_right_choice_2' in request.POST:
                choice_dict['is_right_choice'] = True
            else:
                choice_dict['is_right_choice'] = False
        form_list.append(choice_dict)

        if 'choice_text_3' in request.POST:
            choice_dict = {'choice_text': request.POST['choice_text_3']}
            if 'is_right_choice_3' in request.POST:
                choice_dict['is_right_choice'] = True
            else:
                choice_dict['is_right_choice'] = False
        form_list.append(choice_dict)

        if 'choice_text_4' in request.POST:
            choice_dict = {'choice_text': request.POST['choice_text_4']}
            if 'is_right_choice_4' in request.POST:
                choice_dict['is_right_choice'] = True
            else:
                choice_dict['is_right_choice'] = False
        form_list.append(choice_dict)

        for form in form_list:
            QuestionChoice.objects.create(
                choice=Choice.objects.create(choice_text=form['choice_text'], is_right_choice=form['is_right_choice']),
                question=question,
            )
        return redirect('dashboard.question_pool')


        
    return render(request, 'dashboard/create_question_choice.html', context)