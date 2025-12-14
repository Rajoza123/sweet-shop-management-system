from django.urls import path
from .views import SweetCreateView , SweetListView , SweetPurchaseView , SweetRestockView

urlpatterns = [
    path("create/", SweetCreateView.as_view(), name="sweet-create"),
    path("", SweetListView.as_view(), name="sweet-list"),
    path("<int:pk>/purchase/", SweetPurchaseView.as_view(), name="sweet-purchase"),
    path("<int:pk>/restock/", SweetRestockView.as_view(), name="sweet-restock"),
]
