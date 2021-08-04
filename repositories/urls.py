from django.urls import path
from . import views

urlpatterns = [
    path("", views.repository_view, name="main"),
]

app_name = "repositories"
