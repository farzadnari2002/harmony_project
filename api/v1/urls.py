from django.urls import path, include


urlpatterns = [
    path('account/', include('accounts.api.v1.urls'))
]
