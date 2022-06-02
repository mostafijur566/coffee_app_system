from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('login/', obtain_auth_token),

    path('get-user/<str:pk>/', getRole),

    path('add-coffee/', addCoffee),
    path('get-coffee/', getCoffee),
    path('get-single-item/<str:pk>/', getSingleItem),
    path('update-coffee/<str:pk>/', updateCoffee),

    path('add-recommended-coffee/', addRecommendedCoffee),
    path('get-recommended-coffee/', getRecommendedCoffee),
    path('get-single-recommended-item/<str:pk>/', getSingleRecommendedItem),
    path('update-recommended-coffee/<str:pk>/', updateRecommendedCoffee),

    path('is-favourite/', isFavourite),
    path('get-favourite/', getFavourite),

    path('get-order/', getOrder),
    path('make-order/', makeOrder),
    path('delete-order/<str:pk>/', orderDelete),
]