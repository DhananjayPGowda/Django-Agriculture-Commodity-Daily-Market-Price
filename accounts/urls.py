from django.urls import path
from . import views
urlpatterns = [
    path('/login',views.Login),
    path('/signup',views.signup),
    path('/logout',views.Logout), 
    ]