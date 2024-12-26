from django.urls import path
from . import views

urlpatterns = [
    path("stock/list", views.ListStockView.as_view(), name="list-stock"),
    path("stock/create", views.CreateStockView.as_view(), name="create-stock"),  
    path("stock/edit", views.UpdateView.as_view(), name="update-stock"),
]
