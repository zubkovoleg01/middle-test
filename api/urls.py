from django.urls import path
from . import views


urlpatterns = [
    path('api/<str:phone_number>/', views.number_finder_api, name='number_finder_api'),
]