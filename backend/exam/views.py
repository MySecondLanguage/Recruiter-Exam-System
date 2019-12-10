from django.shortcuts import (
    render,
    HttpResponse
)

# Create your views here.
def exam(request):
    return render(request, 'exam.html')