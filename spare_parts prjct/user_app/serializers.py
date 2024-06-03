from rest_framework import serializers
from .models import *
import random
from django.utils import timezone
from twilio.rest import Client
from django.conf import settings

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['name', 'mobile_number', 'password']

    def create(self, validated_data):
        otp = self.generate_otp()
        user = User(
            name=validated_data['name'],
            mobile_number=validated_data['mobile_number'],
            password=validated_data['password'],  # Note: For production, use password hashing
            otp=otp,
            otp_created_at=timezone.now()
        )
        user.save()

        # Send OTP to user's mobile number
        self.send_otp(user.mobile_number, otp)

        return user

    def generate_otp(self):
        return str(random.randint(100000, 999999))

    def send_otp(self, mobile_number, otp_code):
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        client.messages.create(
            body=f"Your OTP code is {otp_code}",
            from_=settings.TWILIO_PHONE_NUMBER,
            to=mobile_number
        )
class UserupdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'mobile_number', 'password', 'is_active']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['address_id', 'user_id', 'fullname', 'phone_number', 'address', 'pin_code', 'state', 'city', 'landmark']


# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ['product_id', 'title', 'image', 'price', 'vehicle', 'highlights', 'description', 'category', 'year', 'created_at']

# class OrderSerializer(serializers.ModelSerializer):
#     user_id = UserRegistrationSerializer()
#     product_id = ProductSerializer()
#     address_id = AddressSerializer()
#
#     class Meta:
#         model = Order
#         fields = ['order_id', 'user_id', 'product_id', 'address_id', 'quantity', 'total', 'payment_method']
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order_id', 'user_id', 'product_id', 'address_id', 'quantity', 'total', 'payment_method']
