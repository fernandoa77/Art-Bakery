from django.contrib import admin
from .models import Bakery, Ingredient, Material

class BakeryAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'bakery', 'quantity', 'unit', 'cost')
    list_filter = ('bakery',)
    search_fields = ('name',)

class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'bakery', 'quantity', 'unit', 'cost')
    list_filter = ('bakery',)
    search_fields = ('name',)

admin.site.register(Bakery, BakeryAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Material, MaterialAdmin)
