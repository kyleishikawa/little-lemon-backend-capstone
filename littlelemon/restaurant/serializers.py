#define Serializer class for User model
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from .models import Menu, Booking

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password', 'groups']

class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'