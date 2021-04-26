from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('cors/', views.csrf),
    path('', views.HomePageView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('account/', include('backend.user.urls')),
    path('classes/', include('backend.classes.urls'))
    # re_path('^(?!backend)', views.index)
]
