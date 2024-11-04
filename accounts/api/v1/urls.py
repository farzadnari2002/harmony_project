from django.urls import path, include
from .views import CreateUserView


urlpatterns = [
    path('create/', CreateUserView.as_view())
]
