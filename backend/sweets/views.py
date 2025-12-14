from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import Sweet
from .serializers import SweetSerializer
from .filters import SweetFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
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
class SweetPurchaseView(APIView):
    def post(self, request, pk):
        sweet = get_object_or_404(Sweet, pk=pk)

        if sweet.quantity <= 0:
            return Response(
                {"detail": "Out of stock"},
                status=status.HTTP_400_BAD_REQUEST
            )

        sweet.quantity -= 1
        sweet.save()

        return Response(
            {
                "id": sweet.id,
                "name": sweet.name,
                "quantity": sweet.quantity
            },
            status=status.HTTP_200_OK
        )