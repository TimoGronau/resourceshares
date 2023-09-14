from django.urls import path
from . import views
from .views import ResourcePostView

urlpatterns = [
    path('', views.home_page, name="home-page"),
    path("resource/<int:id>", views.resource_detail, name="resource-detail"), #casts the url id into an integer and passes it to resource detail which takes it as an id
    path("resource/post/", ResourcePostView.as_view(), name="resource-post"),
]