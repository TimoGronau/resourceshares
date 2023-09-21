from django.urls import path
from . import views


urlpatterns = [
    path("list/", views.user_list,name="user_list"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    
]