from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Stock, Management
from django.contrib.auth.mixins import LoginRequiredMixin

class StockListView(ListView):
    model = Stock
    template_name = 'stock/stock_list.html'
    context_object_name = 'stocks'

class StockCreateView(LoginRequiredMixin, CreateView):
    model = Stock
    template_name = 'stock/stock_form.html'
    fields = ['stock_name', 'disc', 'price']
    success_url = reverse_lazy('stock:list')

class StockUpdateView(LoginRequiredMixin, UpdateView):
    model = Stock
    template_name = 'stock/stock_form.html'
    fields = ['stock_name', 'disc', 'price']
    success_url = reverse_lazy('stock:list')

class StockDeleteView(LoginRequiredMixin, DeleteView):
    model = Stock
    template_name = 'stock/stock_confirm_delete.html'
    success_url = reverse_lazy('stock:list')

class ManagementListView(ListView):
    model = Management
    template_name = 'stock/management_list.html'
    context_object_name = 'managements'

class ManagementCreateView(LoginRequiredMixin, CreateView):
    model = Management
    template_name = 'stock/management_form.html'
    fields = ['name', 'pieces', 'stock_id', 'customer_id']
    success_url = reverse_lazy('stock:management_list')

    def form_valid(self, form):
        # ログインユーザーを自動的に設定
        form.instance.customer_id = self.request.user.customer
        return super().form_valid(form)

class ManagementUpdateView(LoginRequiredMixin, UpdateView):
    model = Management
    template_name = 'stock/management_form.html'
    fields = ['stock_id', 'pieces']
    success_url = reverse_lazy('stock:management_list')

    def get_queryset(self):
        # ログインユーザーの管理データのみを取得
        return Management.objects.filter(customer_id=self.request.user.customer)