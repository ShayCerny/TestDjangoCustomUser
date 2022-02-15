from django.urls import path

from . import views 

urlpatterns = [
    # /signup
    path('signup', views.signUpView, name="signup"), 
    path('login', views.loginView, name="login"),
    path('logout', views.logoutView, name='logout'),
    # https://localhost:8000/
    path('', views.index, name="home"),
]