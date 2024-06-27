from django.contrib import admin
from .models import Bakery, Ingredient, Material, Labor, FixedExpense, VariableExpense, Customer

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

class LaborAdmin(admin.ModelAdmin):
    list_display = ('name', 'bakery', 'daily_hours', 'days_worked', 'monthly_wage')
    list_filter = ('bakery',)
    search_fields = ('name',)

class FixedExpenseAdmin(admin.ModelAdmin):
    list_display = ('concept', 'bakery', 'monthly_cost')
    list_filter = ('bakery',)
    search_fields = ('concept',)

class VariableExpenseAdmin(admin.ModelAdmin):
    list_display = ('concept', 'bakery', 'date', 'amount')
    list_filter = ('bakery', 'date')
    search_fields = ('concept',)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'bakery', 'address', 'phone', 'email', 'origin')
    list_filter = ('bakery',)
    search_fields = ('name', 'email')

admin.site.register(Bakery, BakeryAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Labor, LaborAdmin)
admin.site.register(FixedExpense, FixedExpenseAdmin)
admin.site.register(VariableExpense, VariableExpenseAdmin)
admin.site.register(Customer, CustomerAdmin)
