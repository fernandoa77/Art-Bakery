from django.urls import path
from . import views

urlpatterns = [
    path('<int:bakery_id>/', views.bakery_main_page, name='bakery_main_page'),
    path('<int:bakery_id>/orders/add/', views.add_order, name='add_order'),
    path('<int:bakery_id>/orders/log/', views.order_log, name='order_log'),
    path('<int:bakery_id>/products/ingredients/', views.ingredients, name='ingredients'),
    path('<int:bakery_id>/products/ingredients/add/', views.add_ingredient, name='add_ingredient'),
    path('<int:bakery_id>/products/ingredients/<int:ingredient_id>/edit/', views.edit_ingredient, name='edit_ingredient'),
    path('<int:bakery_id>/products/ingredients/<int:ingredient_id>/delete/', views.delete_ingredient, name='delete_ingredient'),
    path('<int:bakery_id>/products/recipes/', views.recipes, name='recipes'),
    path('<int:bakery_id>/products/materials/', views.materials, name='materials'),
    path('<int:bakery_id>/products/packages/', views.packages, name='packages'),
    path('<int:bakery_id>/customers/', views.customers, name='customers'),
    path('<int:bakery_id>/expenses/labor-costs/', views.labor_costs, name='labor_costs'),
    path('<int:bakery_id>/expenses/fixed-expenses/', views.fixed_expenses, name='fixed_expenses'),
    path('<int:bakery_id>/expenses/variable-expenses/', views.variable_expenses, name='variable_expenses'),
    path('<int:bakery_id>/reports/expense-report/', views.expense_report, name='expense_report'),
    path('<int:bakery_id>/reports/sales-report/', views.sales_report, name='sales_report'),
    path('<int:bakery_id>/reports/financial-overview/', views.financial_overview, name='financial_overview'),
    path('<int:bakery_id>/configuration/', views.configuration, name='configuration'),
]
