from django.urls import path
from .views import SweetCreateView

urlpatterns = [
    path("create/", SweetCreateView.as_view(), name="sweet-create"),
]
