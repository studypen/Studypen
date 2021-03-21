from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('account/', include('backend.auth.urls')),
    re_path('^(?!backend)', views.index)
]
