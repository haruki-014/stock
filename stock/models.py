from django.db import models
from accounts.models import Customer

class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    stock_name = models.CharField(max_length=100, verbose_name='商品名')
    disc = models.ImageField(null=True, blank=True, verbose_name='商品画像')
    price = models.IntegerField(verbose_name='価格')
    
    def __str__(self):
        return self.stock_name
    
class Management(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='顧客')
    stock_id = models.ForeignKey(Stock, on_delete=models.CASCADE, verbose_name='商品')
    pieces = models.IntegerField(verbose_name='数量')
    
    class Meta:
        # 同じ顧客が同じ商品を重複して管理できないようにする
        unique_together = ('customer_id', 'stock_id')
        verbose_name = '在庫管理'
        verbose_name_plural = '在庫管理'
    
    def __str__(self):
        return f"{self.customer_id} - {self.stock_id} ({self.pieces}個)"