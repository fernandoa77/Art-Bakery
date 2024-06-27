from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden

from .models import Bakery, Ingredient, Material, Labor
from .forms import IngredientForm, MaterialForm , LaborForm


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

# PRODUCT CREATION
# ingredients

@login_required
def ingredients(request, bakery_id):
    bakery = get_object_or_404(Bakery, id=bakery_id)
    if admin_check(request.user) or request.user == bakery.owner:
        ingredients = Ingredient.objects.filter(bakery=bakery)
        return render(request, 'products/ingredients/ingredients.html', {'bakery': bakery, 'ingredients': ingredients})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")

@login_required
def add_ingredient(request, bakery_id):
    bakery = get_object_or_404(Bakery, id=bakery_id)
    if admin_check(request.user) or request.user == bakery.owner:
        if request.method == 'POST':
            form = IngredientForm(request.POST)
            if form.is_valid():
                ingredient = form.save(commit=False)
                ingredient.bakery = bakery
                ingredient.save()
                return redirect('ingredients', bakery_id=bakery.id)
        else:
            form = IngredientForm()
        return render(request, 'products/ingredients/add_ingredient.html', {'form': form, 'bakery': bakery})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")

@login_required
def edit_ingredient(request, bakery_id, ingredient_id):
    bakery = get_object_or_404(Bakery, id=bakery_id)
    ingredient = get_object_or_404(Ingredient, id=ingredient_id, bakery=bakery)
    if admin_check(request.user) or request.user == bakery.owner:
        if request.method == 'POST':
            form = IngredientForm(request.POST, instance=ingredient)
            if form.is_valid():
                form.save()
                return redirect('ingredients', bakery_id=bakery.id)
        else:
            form = IngredientForm(instance=ingredient)
        return render(request, 'products/ingredients/edit_ingredient.html', {'form': form, 'bakery': bakery})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")

@login_required
def delete_ingredient(request, bakery_id, ingredient_id):
    bakery = get_object_or_404(Bakery, id=bakery_id)
    ingredient = get_object_or_404(Ingredient, id=ingredient_id, bakery=bakery)
    if admin_check(request.user) or request.user == bakery.owner:
        if request.method == 'POST':
            ingredient.delete()
            return redirect('ingredients', bakery_id=bakery.id)
        return render(request, 'products/ingredients/delete_ingredient.html', {'ingredient': ingredient, 'bakery': bakery})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")

#materials

@login_required
def materials(request, bakery_id):
    bakery = get_object_or_404(Bakery, id=bakery_id)
    if admin_check(request.user) or request.user == bakery.owner:
        materials = Material.objects.filter(bakery=bakery)
        return render(request, 'products/materials/materials.html', {'bakery': bakery, 'materials': materials})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")

@login_required
def add_material(request, bakery_id):
    bakery = get_object_or_404(Bakery, id=bakery_id)
    if admin_check(request.user) or request.user == bakery.owner:
        if request.method == 'POST':
            form = MaterialForm(request.POST)
            if form.is_valid():
                material = form.save(commit=False)
                material.bakery = bakery
                material.save()
                return redirect('materials', bakery_id=bakery.id)
        else:
            form = MaterialForm()
        return render(request, 'products/materials/add_material.html', {'form': form, 'bakery': bakery})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")

@login_required
def edit_material(request, bakery_id, material_id):
    bakery = get_object_or_404(Bakery, id=bakery_id)
    material = get_object_or_404(Material, id=material_id, bakery=bakery)
    if admin_check(request.user) or request.user == bakery.owner:
        if request.method == 'POST':
            form = MaterialForm(request.POST, instance=material)
            if form.is_valid():
                form.save()
                return redirect('materials', bakery_id=bakery.id)
        else:
            form = MaterialForm(instance=material)
        return render(request, 'products/materials/edit_material.html', {'form': form, 'bakery': bakery})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")

@login_required
def delete_material(request, bakery_id, material_id):
    bakery = get_object_or_404(Bakery, id=bakery_id)
    material = get_object_or_404(Material, id=material_id, bakery=bakery)
    if admin_check(request.user) or request.user == bakery.owner:
        if request.method == 'POST':
            material.delete()
            return redirect('materials', bakery_id=bakery.id)
        return render(request, 'products/materials/delete_material.html', {'material': material, 'bakery': bakery})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")



#recipes
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
#labor
@login_required
def labor_list(request, bakery_id):
    bakery = get_object_or_404(Bakery, id=bakery_id)
    if admin_check(request.user) or request.user == bakery.owner:
        labor_list = Labor.objects.filter(bakery=bakery)
        return render(request, 'expenses/labor/labor.html', {'bakery': bakery, 'labor_list': labor_list})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")

@login_required
def add_labor(request, bakery_id):
    bakery = get_object_or_404(Bakery, id=bakery_id)
    if admin_check(request.user) or request.user == bakery.owner:
        if request.method == 'POST':
            form = LaborForm(request.POST)
            if form.is_valid():
                labor = form.save(commit=False)
                labor.bakery = bakery
                labor.save()
                return redirect('labor_list', bakery_id=bakery.id)
        else:
            form = LaborForm()
        return render(request, 'expenses/labor/add_labor.html', {'form': form, 'bakery': bakery})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")

@login_required
def edit_labor(request, bakery_id, labor_id):
    bakery = get_object_or_404(Bakery, id=bakery_id)
    labor = get_object_or_404(Labor, id=labor_id, bakery=bakery)
    if admin_check(request.user) or request.user == bakery.owner:
        if request.method == 'POST':
            form = LaborForm(request.POST, instance=labor)
            if form.is_valid():
                form.save()
                return redirect('labor_list', bakery_id=bakery.id)
        else:
            form = LaborForm(instance=labor)
        return render(request, 'expenses/labor/edit_labor.html', {'form': form, 'bakery': bakery})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")

@login_required
def delete_labor(request, bakery_id, labor_id):
    bakery = get_object_or_404(Bakery, id=bakery_id)
    labor = get_object_or_404(Labor, id=labor_id, bakery=bakery)
    if admin_check(request.user) or request.user == bakery.owner:
        if request.method == 'POST':
            labor.delete()
            return redirect('labor_list', bakery_id=bakery.id)
        return render(request, 'expenses/labor/delete_labor.html', {'labor': labor, 'bakery': bakery})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")
    
#expenses

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