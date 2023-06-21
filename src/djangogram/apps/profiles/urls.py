from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile_view, name='profile'),
    path('register/', views.register, name='register'),
]
