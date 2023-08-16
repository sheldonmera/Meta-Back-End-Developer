from rest_framework import serializers
from .models import Menu, Booking



class MenuSerializer(serializers.ModelSerializer):

    class Meta():
        model = Menu
        fields = ['id','title','price','featured','category']
        depth = 1
        
class BookingSerializer(serializers.ModelSerializer):

    class Meta():
        model = Booking
        fields = ['id','first_name','reservation_date','reservation_slot',]
        depth = 1


