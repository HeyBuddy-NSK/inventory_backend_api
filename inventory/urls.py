from django.contrib import admin
from django.urls import path, include
from .views import CreateItemView, ItemDetailView, ListAllItems

urlpatterns = [
    path('items/',CreateItemView.as_view(), name='create_item'),
    path('items/all/',ListAllItems.as_view(), name='list_items'),
    path('items/<int:pk>/',ItemDetailView.as_view(), name='item_detail')
]