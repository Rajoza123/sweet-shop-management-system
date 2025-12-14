from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import Sweet
from .serializers import SweetSerializer
from .filters import SweetFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
class SweetCreateView(generics.CreateAPIView):
    queryset = Sweet.objects.all()
    serializer_class = SweetSerializer
    permission_classes = [IsAdminUser]
class SweetListView(generics.ListAPIView):
    queryset = Sweet.objects.all()
    serializer_class = SweetSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = SweetFilter
    search_fields = ["name"]