from . import views
from django.urls import path

urlpatterns = [
    path('api/', views.movie_list),
    path('api/<int:pk>/', views.movie_detail),
]