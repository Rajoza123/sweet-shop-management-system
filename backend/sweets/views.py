from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import Sweet
from .serializers import SweetSerializer

class SweetCreateView(generics.CreateAPIView):
    queryset = Sweet.objects.all()
    serializer_class = SweetSerializer
    permission_classes = [IsAdminUser]
