from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/', views.bakery_main_page, name='bakery_main_page'),
    path('<str:username>/orders/add/', views.add_order, name='add_order'),
    path('<str:username>/orders/log/', views.order_log, name='order_log'),
    path('<str:username>/products/ingredients/', views.ingredients, name='ingredients'),
    path('<str:username>/products/recipes/', views.recipes, name='recipes'),
    path('<str:username>/products/materials/', views.materials, name='materials'),
    path('<str:username>/products/packages/', views.packages, name='packages'),
    path('<str:username>/customers/', views.customers, name='customers'),
    path('<str:username>/expenses/labor-costs/', views.labor_costs, name='labor_costs'),
    path('<str:username>/expenses/fixed-expenses/', views.fixed_expenses, name='fixed_expenses'),
    path('<str:username>/expenses/variable-expenses/', views.variable_expenses, name='variable_expenses'),
    path('<str:username>/reports/expense-report/', views.expense_report, name='expense_report'),
    path('<str:username>/reports/sales-report/', views.sales_report, name='sales_report'),
    path('<str:username>/reports/financial-overview/', views.financial_overview, name='financial_overview'),
    path('<str:username>/configuration/', views.configuration, name='configuration'),
]