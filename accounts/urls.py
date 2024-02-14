from django.urls import path,include
from . import views

urlpatterns = [
    path('signup/',views.signupView.as_view(),name='signup' )
]