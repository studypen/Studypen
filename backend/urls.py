from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('account/', include('backend.user.urls')),
    path('classes/', include('backend.classes.urls'))
]
