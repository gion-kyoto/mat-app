from django.urls import path
from match_app import views

urlpatterns = [
    path('', views.home, name='home'),
]
