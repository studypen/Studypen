from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse
from django.views.generic import TemplateView

@ensure_csrf_cookie
def index(request):
  return render(request, 'index.html')

# @ensure_csrf_cookie
class HomePageView(TemplateView):
    template_name = 'index.html'