from django.urls import path, include


urlpatterns = [
    path('user/', include('accounts.api.v1.urls'))
]
