from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *
from spare_part_app.serializers import *

class UserRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully. OTP sent to mobile number."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserUpdateView(APIView):
    def put(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserupdateSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddressListCreateView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
