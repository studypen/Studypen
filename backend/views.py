from django.shortcuts import redirect
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def index(request):
    return redirect('https://www.studypen.in/')
