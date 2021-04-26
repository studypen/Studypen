from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt import serializers
# from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', views.MyTokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', views.logout_view),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('user/', views.uesr_view),

    path('update/', views.UpdateView.as_view()),  # by old pass

    # path('password/change/', ),# by old pass
    # path('password/reset/', ), # by email
    # path('reset/confirm/', ),  # from email
    # path('register/verify-email/', ),

    # path('register/google/', ),
]
