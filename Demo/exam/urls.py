from django.urls import path
from exam import views


urlpatterns = [
    path('about', views.about)
]