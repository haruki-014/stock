from django.shortcuts import render

# Create your views here.

from .models import Stock, Management

from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    DeleteView,
    UpdateView,
)

class ListStockView(ListView):
    template_name = "stock/stock_list.html"
    model = Stock


class CreateStockView(CreateView):
    template_name = "stock/stock_create.html"
    model = Stock
    fields = ("id", "stock_name", "disc", "price")
    
class UpdateStockView(UpdateView):
    template_name = "stock/stock_edit.html"
    model = Stock
    

    
def index_view(request):
    object_list = Stock.objects.order_by("-id")
    
   
    
    return render (
        request,
        "base.html",
        {"object_list": object_list},
    )