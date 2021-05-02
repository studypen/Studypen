from django.shortcuts import redirect
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import TemplateView


@ensure_csrf_cookie
def index(request):
    # render(request, 'index.html')
    return redirect('https://www.studypen.in/')


@ensure_csrf_cookie
def csrf(request):
    return {'status': 'ok'}
# @ensure_csrf_cookie

