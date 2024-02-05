from django.urls import path
from .views import UserLoginAPi, UserRegisterAPi

"""
    
"""

urlpatterns = [
    path("register/", UserRegisterAPi.as_view()),
    path("login/", UserLoginAPi.as_view())
]

