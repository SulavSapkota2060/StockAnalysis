from django.contrib import admin
from .models import Todo,Just, UpStat, Stocks

# Register your models here.


admin.site.register(Todo)
admin.site.register(Just)
admin.site.register(UpStat)
admin.site.register(Stocks)