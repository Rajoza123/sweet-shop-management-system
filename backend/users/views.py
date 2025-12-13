from rest_framework import generics , status
from rest_framework.response import Response
from .serializers import RegisterSerializer , LoginSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from django.db import IntegrityError

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            return Response({
                "id": user.id,
                "username": user.username,
                "email": user.email
            }, status=status.HTTP_201_CREATED)

        except IntegrityError:
            return Response(
                {"detail": "Username or email already exists"},
                status=status.HTTP_400_BAD_REQUEST
            )    
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            tokens = serializer.validated_data

            return Response(tokens, status=status.HTTP_200_OK)

        except Exception:
            return Response(
                {"detail": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )