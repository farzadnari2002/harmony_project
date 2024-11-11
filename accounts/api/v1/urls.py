from django.urls import path
from .views import *
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )


urlpatterns = [
    path('login/', LoginView.as_view()),
    path('verify/', OtpVerifyView.as_view()),
    path('', UserInfoView.as_view()),
    path('edit/', UserEditView.as_view()),       
]
