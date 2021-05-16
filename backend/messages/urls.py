from django.urls import path
from . import views

urlpatterns = [
    path('class/', views.ClassMessageAPIView.as_view())
    # path('', views.ClassesAPIView.as_view()),
    # path('shedule/', views.SheduleTimeAPIView.as_view()),
    # path('invite/', views.inviteLinks),
    # path('join/', views.join),

]
