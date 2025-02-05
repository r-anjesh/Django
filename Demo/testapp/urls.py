from django.urls import path
from testapp import views

urlpatterns = [
    path('home', views.home),
    path('hello', views.greetings),
    path('contact', views.contact),
    path('add/', views.add_employee, name='add_employee'),
    path('employee_list/', views.employee_list, name='employee_list'),
]