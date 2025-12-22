from django.urls import path
from .views import SweetCreateView , SweetListView , SweetPurchaseView , SweetRestockView , SweetDetailView , SweetUpdateView , SweetDeleteView

urlpatterns = [
    path("create/", SweetCreateView.as_view(), name="sweet-create"),
    path("", SweetListView.as_view(), name="sweet-list"),
    path("<int:pk>/purchase/", SweetPurchaseView.as_view(), name="sweet-purchase"),
    path("<int:pk>/restock/", SweetRestockView.as_view(), name="sweet-restock"),
    path("<int:pk>/", SweetDetailView.as_view(), name="sweet-detail"),
    path("<int:pk>/update/", SweetUpdateView.as_view(), name="sweet-update"),
    path("<int:pk>/delete/", SweetDeleteView.as_view(), name="sweet-delete"),
    path("", SweetListView.as_view(), name="sweet-list"),
]
