from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    path("", views.IndexClassView.as_view(), name='index'),
    path("<int:pk>/", views.DetailClassView.as_view(), name="detail"),
    path("add", views.CreateItem.as_view(), name="create_item"),
    path('update/', views.update_item_list, name='update_item_list'),
    path('update/<int:id>', views.update_item, name='update_item'),
    path('delete/<int:id>', views.delete_item, name='delete_item'),
]