from . import views
from django.urls import path

urlpatterns = [
    path("api/", views.MovieList.as_view(), name=""),
    path('api/<int:pk>/',views.MovieDetail.as_view()),
]