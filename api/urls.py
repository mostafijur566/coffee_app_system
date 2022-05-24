from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('login/', obtain_auth_token),
    path('get-coffee/', getCoffee),
    path('get-user/<str:pk>/', getRole),
]