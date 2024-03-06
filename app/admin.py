from django.contrib import admin

# Register your models here.

from app.models import *

class cust(admin.ModelAdmin):
    list_display = ['id','pro_name','pro_price','pro_brand']

admin.site.register(Product,cust)