from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.HomePage.as_view(), name='home')
]