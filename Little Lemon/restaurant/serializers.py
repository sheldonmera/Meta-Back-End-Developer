from rest_framework import serializers
from .models import MenuItem, Category
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class MenuItemSerializer(serializers.ModelSerializer):

    class Meta():
        model = MenuItem
        fields = ['id','title','price','featured','category']
        depth = 1

class CategorySerializer(serializers.ModelSerializer):
    class Meta():
        model = Category
        fields = ['slug']

class SingleHelperSerializer(serializers.ModelSerializer):
    class Meta():
        model = MenuItem
        fields = ['title','price']
