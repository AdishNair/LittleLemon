from rest_framework import serializers

from .models import Booking, Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title', 'price', 'inventory']


class MenuItemSerializer(MenuSerializer):
    """Compatibility name used by the supplied course examples."""


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
