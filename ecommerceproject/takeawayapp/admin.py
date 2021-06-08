from django.contrib import admin

# Register your models here.
from .models import Category, Restourent, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'slug']
    prepopulated_fields = {'slug': ('category_name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_price', 'stock', 'available', 'created', 'updated']
    list_editable = ['product_price', 'stock']
    prepopulated_fields = {'slug': ('product_name',)}
    # list_per_page = 20


admin.site.register(Product, ProductAdmin)


class RestourentAdmin(admin.ModelAdmin):
    list_display = ['restourent_name', 'location', 'open']
    list_editable = ['open']
    prepopulated_fields = {'slug': ('restourent_name',)}


admin.site.register(Restourent, RestourentAdmin)
