from django.contrib.auth.models import AnonymousUser

from exam.models import Exam

# Middlware to access person in request
class ExamMiddleWare(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            exam = Exam.objects.filter(is_published=True).first()
            request.current_exam = exam
            response = self.get_response(request)
            return response
        else:
            exam = Exam.objects.filter(is_published=True).first()
            request.current_exam = exam
            response = self.get_response(request)
            return response