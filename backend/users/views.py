from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = self.get_serializer().instance

        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email
        }, status=status.HTTP_201_CREATED)
