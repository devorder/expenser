from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterationView.as_view(), name="register"),
    path('validate-user/', views.UserNameValidationView.as_view(), name="validate-user"),
    path('login/', views.RegisterationView.as_view(), name="login"),
]
