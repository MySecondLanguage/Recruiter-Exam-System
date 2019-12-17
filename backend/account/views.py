from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.db.models import F, Value, Case, When, BooleanField, Prefetch

from account.models import Profile
from account.enum_helper import UserType

from exam.models import (
    QuestionGroup,
    QuestionChoice,
    Question,
    Exam,
    SelectedChoices,
    Choice
)

def home(request):
    if request.POST:
        name = request.POST['name']
        email = str(request.POST['email'])
        password = str(request.POST['email'])
        username = str(email).split('@')[0]

        created_user = User.objects.create_user(
            username,
            email,
            password
        )
        Profile.objects.create(
            user=created_user,
            user_type=UserType.EXAMINEE.value
        )

        user = authenticate(request, email=email, username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect('exam')
    else:
        return render(request, 'frontstage/index.html')


# def report(request):
#     context = {}

#     # choices = Choice.objects.annotate(
#     #     is_selected_choice=Case(
#     #         When(
#     #             selected_choice__choice__is_right_choice=True,
#     #             then=Value(True)
#     #         ),
#     #         default=Value(False),
#     #         output_field=BooleanField()
#     #     )
#     # )

#     # print(choices)

#     question = Question.objects.filter(
#         exam__id=request.current_exam.id
#     ).prefetch_related('selected_choice')
#     print(question, '-----------------')
#     context['question'] = question
#     return render(request, 'frontstage/report.html', context)


def report(request):
    context = {}

    choices = SelectedChoices.objects.filter(
        user_id=request.user.id,
        exam_id=request.current_exam.id
    )


    print(choices)

    question = Question.objects.filter(
        exam__id=request.current_exam.id
    ).prefetch_related(Prefetch('selected_choice', queryset=choices))
    context['question'] = question
    return render(request, 'frontstage/report.html', context)