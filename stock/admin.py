from django.contrib import admin

# Register your models here.

from .models import Stock, Management

admin.site.register(Stock)
admin.site.register(Management)

