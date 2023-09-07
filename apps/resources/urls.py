from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home-page"),
    path("resource/<int:id>", views.resource_detail, name="resource-detail"), #casts the url id into an integer and passes it to resource detail which takes it as an id
]