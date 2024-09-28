from django.shortcuts import render
from .models import Item
from .serializers import ItemSerializer, UserSerializer
from django.core.cache import cache
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User
import logging

# logger instance
logger = logging.getLogger('inventory')

# Register
class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

# List all items ['GET']
class ListAllItems(generics.ListAPIView):
    """
    class view to get all items.
    """
    logger.info(f"GET request received to fetch all items.")
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    # permission_classes = []
    permission_classes = [IsAuthenticated]

# Create your views here. ['POST']
class CreateItemView(generics.CreateAPIView):
    """
    VIEW class to perform POST
    """
    logger.info(f"POST request received to create a new item.")
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    view class to perform GET, PUT, DELETE.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    # ['GET']
    def retrieve(self, request, *args, **kwargs):
        """
        method to get the item.
        """
        item_pk = kwargs['pk']
        logger.info(f"GET request for item ID {item_pk}")
        cached_item = cache.get(item_pk)

        if cached_item:
            return Response(cached_item)
        
        try:

            response = super().retrieve(request, *args, **kwargs)
            cache.set(item_pk, response.data, timeout=60*15)
            return response
        except Item.DoesNotExist:
            logger.error(f"Item with ID {item_pk} not found.")
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        
    # ['PUT']

    def update(self, request, *args, **kwargs):
        """
        method to update the item.
        """
        logger.info(f"PUT request to update item ID {kwargs['pk']}")
        try:
            logger.info(f"Updatiing item with ID {kwargs['pk']}")
            return super().update(request, *args, **kwargs)
        
        
        except Item.DoesNotExist:
            logger.error(f"Item with ID {kwargs['pk']} not found.")
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        
    # ['DELETE']
    def destroy(self, request, *args, **kwargs):
        """
        method to delete the item.
        """
        logger.info(f"DELETE request to delete item ID {kwargs['pk']}")
        try:
            logger.info(f"Deleting item with ID {kwargs['pk']}")
            return super().destroy(request, *args, **kwargs)
        
        except Item.DoesNotExist:
            logger.error(f"Item with ID {kwargs['pk']} not found.")
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

    
