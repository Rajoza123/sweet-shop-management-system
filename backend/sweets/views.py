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
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework.exceptions import ValidationError

from django.shortcuts import get_object_or_404
from .services import restock_sweet

from .services import purchase_sweet
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
        try:
            sweet = purchase_sweet(pk)
        except ValidationError as e:
            return Response(
                {"detail": str(e.detail[0])},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception:
            raise Http404

        return Response(
            {
                "id": sweet.id,
                "name": sweet.name,
                "quantity": sweet.quantity
            },
            status=status.HTTP_200_OK
        )
class SweetRestockView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request, pk):
        try:
            amount = int(request.data.get("amount"))
            sweet = restock_sweet(pk, amount)
        except (TypeError, ValueError):
            return Response(
                {"detail": "Invalid amount"},
                status=status.HTTP_400_BAD_REQUEST
            )
        except ValidationError as e:
            return Response(
                {"detail": str(e.detail[0])},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception:
            raise Http404

        return Response(
            {
                "id": sweet.id,
                "name": sweet.name,
                "quantity": sweet.quantity
            },
            status=status.HTTP_200_OK
        )
        
class SweetDetailView(generics.RetrieveAPIView):
    serializer_class = SweetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Sweet.objects.all()