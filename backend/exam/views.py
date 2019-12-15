from django.shortcuts import (
    render,
    HttpResponse
)
from django.shortcuts import redirect

# Create your views here.
def exam(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect('/')