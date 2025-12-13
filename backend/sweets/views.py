from rest_framework import generics, status
from rest_framework.response import Response
from .models import Sweet
from .serializers import SweetSerializer
from .permissions import IsAdminUser

class SweetCreateView(generics.CreateAPIView):
    queryset = Sweet.objects.all()
    serializer_class = SweetSerializer
    permission_classes = [IsAdminUser]
