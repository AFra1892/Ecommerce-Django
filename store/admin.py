from django.contrib import admin
from .models import Product , Variant

# Register your models here.

class VariantInline(admin.TabularInline):
    model = Variant
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name' , 'brand' , 'base_price' , 'is_active')
    inlines = [VariantInline]
