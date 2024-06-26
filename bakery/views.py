from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from .models import Bakery, Ingredient

def admin_check(user):
    return user.groups.filter(name='admins').exists()

def pastelero_check(user):
    return user.groups.filter(name='pasteleros').exists()


def home_redirect(request):
    try:
        bakery = Bakery.objects.get(owner=request.user)
        return redirect(f'/bakery/{bakery.id}')
    except Bakery.DoesNotExist:
        return HttpResponseForbidden("You do not own a bakery.")

@login_required
def bakery_main_page(request, bakery_id):
    bakery = get_object_or_404(Bakery, id=bakery_id)
    if admin_check(request.user) or request.user == bakery.owner:
        return render(request, 'bakery_main_page.html', {'bakery': bakery})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")

def logout_view(request):
    logout(request)
    return redirect('login')

# Orders views
@login_required
def add_order(request, bakery_id):
    bakery = get_object_or_404(Bakery, id=bakery_id)
    if admin_check(request.user) or request.user == bakery.owner:
        return render(request, 'orders/add_order.html', {'bakery': bakery})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")

@login_required
def order_log(request, bakery_id):
    bakery = get_object_or_404(Bakery, id=bakery_id)
    if admin_check(request.user) or request.user == bakery.owner:
        # Placeholder for fetching orders from the database
        orders = []  # Replace with actual query to get orders
        return render(request, 'orders/order_log.html', {'bakery': bakery, 'orders': orders})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")

# Product creation views
@login_required
def ingredients(request, bakery_id):
    bakery = get_object_or_404(Bakery, id=bakery_id)
    if admin_check(request.user) or request.user == bakery.owner:
        # Fetch ingredients from the database
        ingredients = Ingredient.objects.filter(bakery=bakery)
        return render(request, 'products/ingredients.html', {'bakery': bakery, 'ingredients': ingredients})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")


@login_required
def recipes(request, bakery_id):
    bakery = get_object_or_404(Bakery, id=bakery_id)
    if admin_check(request.user) or request.user == bakery.owner:
        # Placeholder for fetching recipes from the database
        recipes = []  # Replace with actual query to get recipes
        return render(request, 'products/recipes.html', {'bakery': bakery, 'recipes': recipes})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")

@login_required
def materials(request, bakery_id):
    bakery = get_object_or_404(Bakery, id=bakery_id)
    if admin_check(request.user) or request.user == bakery.owner:
        # Placeholder for fetching materials from the database
        materials = []  # Replace with actual query to get materials
        return render(request, 'products/materials.html', {'bakery': bakery, 'materials': materials})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")

@login_required
def packages(request, bakery_id):
    bakery = get_object_or_404(Bakery, id=bakery_id)
    if admin_check(request.user) or request.user == bakery.owner:
        # Placeholder for fetching packages from the database
        packages = []  # Replace with actual query to get packages
        return render(request, 'products/packages.html', {'bakery': bakery, 'packages': packages})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")

# Customers views
@login_required
def customers(request, bakery_id):
    bakery = get_object_or_404(Bakery, id=bakery_id)
    if admin_check(request.user) or request.user == bakery.owner:
        # Placeholder for fetching customers from the database
        customers = []  # Replace with actual query to get customers
        return render(request, 'customers.html', {'bakery': bakery, 'customers': customers})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")

# Expenses views
@login_required
def labor_costs(request, bakery_id):
    bakery = get_object_or_404(Bakery, id=bakery_id)
    if admin_check(request.user) or request.user == bakery.owner:
        return render(request, 'expenses/labor_costs.html', {'bakery': bakery})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")

@login_required
def fixed_expenses(request, bakery_id):
    bakery = get_object_or_404(Bakery, id=bakery_id)
    if admin_check(request.user) or request.user == bakery.owner:
        return render(request, 'expenses/fixed_expenses.html', {'bakery': bakery})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")

@login_required
def variable_expenses(request, bakery_id):
    bakery = get_object_or_404(Bakery, id=bakery_id)
    if admin_check(request.user) or request.user == bakery.owner:
        return render(request, 'expenses/variable_expenses.html', {'bakery': bakery})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")

# Reports views
@login_required
def expense_report(request, bakery_id):
    bakery = get_object_or_404(Bakery, id=bakery_id)
    if admin_check(request.user) or request.user == bakery.owner:
        return render(request, 'reports/expense_report.html', {'bakery': bakery})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")

@login_required
def sales_report(request, bakery_id):
    bakery = get_object_or_404(Bakery, id=bakery_id)
    if admin_check(request.user) or request.user == bakery.owner:
        return render(request, 'reports/sales_report.html', {'bakery': bakery})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")

@login_required
def financial_overview(request, bakery_id):
    bakery = get_object_or_404(Bakery, id=bakery_id)
    if admin_check(request.user) or request.user == bakery.owner:
        return render(request, 'reports/financial_overview.html', {'bakery': bakery})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")

# Configuration views
@login_required
def configuration(request, bakery_id):
    bakery = get_object_or_404(Bakery, id=bakery_id)
    if admin_check(request.user) or request.user == bakery.owner:
        return render(request, 'configuration.html', {'bakery': bakery})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")