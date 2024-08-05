from django.urls import path, include
from .views import authview, home, submit_form, user_form_view

urlpatterns = [
     path("" , home  , name="home"),
     path("signup/" , authview , name="authView"),
     path("accounts/", include("django.contrib.auth.urls")),
     path('form/', user_form_view, name='user_form'),
     path('submit-form/', submit_form, name='submit_form'),
]

