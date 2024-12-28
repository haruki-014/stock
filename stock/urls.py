# from django.urls import path
# from . import views
# 
# urlpatterns = [
#     path("stock/list", views.ListStockView.as_view(), name="list-stock"),
#     path("stock/create", views.CreateStockView.as_view(), name="create-stock"),  
#     path("stock/edit", views.UpdateView.as_view(), name="update-stock"),
# ]


from django.urls import path
from . import views

app_name = 'stock'

urlpatterns = [
    # Stock URLs
    path('', views.StockListView.as_view(), name='list'),
    path('create/', views.StockCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.StockUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.StockDeleteView.as_view(), name='delete'),
    
    # Management URLs
    path('management/', views.ManagementListView.as_view(), name='management_list'),
    path('management/create/', views.ManagementCreateView.as_view(), name='management_create'),
]