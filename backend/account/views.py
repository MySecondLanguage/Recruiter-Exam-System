from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect

from account.models import Profile
from account.enum_helper import UserType

from exam.models import (
    QuestionGroup,
    QuestionChoice,
    Question,
    Exam
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


def report(request):
    # exam = Exam.objects.all().values('id', 'questions__choices')
    # for e in exam:
    #     print(e.question, '-------------------------------------------')
    return render(request, 'frontstage/report.html')