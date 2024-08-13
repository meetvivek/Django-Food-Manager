from django.urls import path
from . import views

# app_name = 'food'
urlpatterns = [
    # path('', views.index, name='index'),  #FUNCTION BASED VIEW
    path('', views.IndexClassView.as_view(), name='index'),  #CLASS BASED VIEW
    # Views Details of an Item
    # path('<int:item_id>/', views.detail, name='detail'),  #FUNCTION BASED VIEW
    path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),  #CLASS BASED VIEW
    path('item/', views.item, name='item'),
    # Add Items
    # path('add/', views.create_item, name="create_item"),  #FUNCTION BASED VIEW
    path('add/', views.CreateItem.as_view(), name="create_item"),  #CLASS BASED VIEW
    # Edit Items
    path('update/<int:id>/', views.update_item, name="update_item"),
    # Delete Items
    path('delete/<int:id>/', views.delete_item, name="delete_item"),
]