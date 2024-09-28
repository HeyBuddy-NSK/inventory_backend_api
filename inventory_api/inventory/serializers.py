from rest_framework import serializers
from .models import Item
from django.contrib.auth.models import User

class ItemSerializer(serializers.ModelSerializer):
    """
    Item data serializer.
    """
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'item_id','price', 'quantity', 'created_at', 'updated_at']

class UserSerializer(serializers.ModelSerializer):
    """
    user data serializer.
    """
    class Meta:
        model = User
        fields = ['username','password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
        