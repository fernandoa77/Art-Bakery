from django.urls import path
from . import views

urlpatterns = [
    #main
    path('<int:bakery_id>/', views.bakery_main_page, name='bakery_main_page'),
    #orders
    path('<int:bakery_id>/orders/add/', views.add_order, name='add_order'),
    path('<int:bakery_id>/orders/log/', views.order_log, name='order_log'),
    #products
    #ingredients
    path('<int:bakery_id>/products/ingredients/', views.ingredients, name='ingredients'),
    path('<int:bakery_id>/products/ingredients/add/', views.add_ingredient, name='add_ingredient'),
    path('<int:bakery_id>/products/ingredients/<int:ingredient_id>/edit/', views.edit_ingredient, name='edit_ingredient'),
    path('<int:bakery_id>/products/ingredients/<int:ingredient_id>/delete/', views.delete_ingredient, name='delete_ingredient'),
    #materials
    path('<int:bakery_id>/products/materials/', views.materials, name='materials'),
    path('<int:bakery_id>/products/materials/add/', views.add_material, name='add_material'),
    path('<int:bakery_id>/products/materials/<int:material_id>/edit/', views.edit_material, name='edit_material'),
    path('<int:bakery_id>/products/materials/<int:material_id>/delete/', views.delete_material, name='delete_material'),
    #receipes
    path('<int:bakery_id>/products/recipes/', views.recipes, name='recipes'),
    #packages
    path('<int:bakery_id>/products/packages/', views.packages, name='packages'),
    #customers
    path('<int:bakery_id>/customers/', views.customers, name='customers'),
    #expenses
    #labor
    path('<int:bakery_id>/labor/', views.labor_list, name='labor_list'),
    path('<int:bakery_id>/labor/add/', views.add_labor, name='add_labor'),
    path('<int:bakery_id>/labor/<int:labor_id>/edit/', views.edit_labor, name='edit_labor'),
    path('<int:bakery_id>/labor/<int:labor_id>/delete/', views.delete_labor, name='delete_labor'),
    #overhead
    path('<int:bakery_id>/expenses/overhead/', views.overhead_expenses, name='overhead_expenses'),
    path('<int:bakery_id>/expenses/fixed/add/', views.add_fixed_expense, name='add_fixed_expense'),
    path('<int:bakery_id>/expenses/fixed/<int:expense_id>/edit/', views.edit_fixed_expense, name='edit_fixed_expense'),
    path('<int:bakery_id>/expenses/fixed/<int:expense_id>/delete/', views.delete_fixed_expense, name='delete_fixed_expense'),
    path('<int:bakery_id>/expenses/variable/add/', views.add_variable_expense, name='add_variable_expense'),
    path('<int:bakery_id>/expenses/variable/<int:expense_id>/edit/', views.edit_variable_expense, name='edit_variable_expense'),
    path('<int:bakery_id>/expenses/variable/<int:expense_id>/delete/', views.delete_variable_expense, name='delete_variable_expense'),
    #eports
    path('<int:bakery_id>/reports/expense-report/', views.expense_report, name='expense_report'),
    path('<int:bakery_id>/reports/sales-report/', views.sales_report, name='sales_report'),
    path('<int:bakery_id>/reports/financial-overview/', views.financial_overview, name='financial_overview'),
    #config
    path('<int:bakery_id>/configuration/', views.configuration, name='configuration'),
]
