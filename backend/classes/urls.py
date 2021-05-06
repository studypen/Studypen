from django.urls import path
from . import views

urlpatterns = [
    # create class
    path('', views.ClassesAPIView.as_view()),
    path('shedule/', views.SheduleTimeAPIView.as_view())
    # path('create/', views.create_class),

    # create time table

    # send joining request

    # accept students

    # all created class and joined class

    # modify time table only creater can

    # make holiday turn off notification for all student and self for the day

    # reshedule class reason



    # path('', views.HomePageView.as_view(), name='home'),
    # path('admin/', admin.site.urls),
    # path('account/', include('backend.user.urls')),
    # path('classes/', include('backend.classes.urls')),
    # re_path('^(?!backend)', views.index)
]
