from django.urls import path
from .views import SweetCreateView , SweetListView

urlpatterns = [
    path("create/", SweetCreateView.as_view(), name="sweet-create"),
    path("", SweetListView.as_view(), name="sweet-list"),
]
