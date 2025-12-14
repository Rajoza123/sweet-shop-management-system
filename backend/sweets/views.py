from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import Sweet
from .serializers import SweetSerializer

class SweetCreateView(generics.CreateAPIView):
    queryset = Sweet.objects.all()
    serializer_class = SweetSerializer
    permission_classes = [IsAdminUser]
class SweetListView(generics.ListAPIView):
    serializer_class = SweetSerializer

    def get_queryset(self):
        queryset = Sweet.objects.all()

        category = self.request.query_params.get("category")
        min_price = self.request.query_params.get("min_price")
        max_price = self.request.query_params.get("max_price")
        name = self.request.query_params.get("name")

        if category:
            queryset = queryset.filter(category=category)

        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset