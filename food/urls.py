from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Views Details of an Item
    path('<int:item_id>/', views.detail, name='detail'),
    path('item/', views.item, name='item'),
    # Add Items
    path('add/', views.create_item, name="create_item"),
    # Edit Items
    path('update/<int:id>/', views.update_item, name="update_item"),
    # Delete Items
    path('delete/<int:id>/', views.delete_item, name="delete_item"),
]