from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden

def admin_check(user):
    return user.groups.filter(name='admins').exists()

def pastelero_check(user):
    return user.groups.filter(name='pasteleros').exists()


@login_required
def home_redirect(request):

    return redirect(f'/bakery/{request.user.username}')

@login_required
def bakery_main_page(request, username):
    user = get_object_or_404(User, username=username)
    if admin_check(request.user) or request.user == user:
        return render(request, 'bakery_main_page.html', {'username': user.username})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")
    
def logout_view(request):
    logout(request)
    return redirect('login')

#orders views
@login_required
def add_order(request, username):
    user = get_object_or_404(User, username=username)
    if admin_check(request.user) or request.user == user:
        return render(request, 'orders/add_order.html', {'username': user.username})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")

@login_required
def order_log(request, username):
    user = get_object_or_404(User, username=username)
    if admin_check(request.user) or request.user == user:
        # Placeholder for fetching orders from the database
        orders = []  # Replace with actual query to get orders
        return render(request, 'orders/order_log.html', {'username': user.username, 'orders': orders})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")
    
#product creation views  
@login_required
def ingredients(request, username):
    user = get_object_or_404(User, username=username)
    if admin_check(request.user) or request.user == user:
        # Placeholder for fetching ingredients from the database
        ingredients = []  # Replace with actual query to get ingredients
        return render(request, 'products/ingredients.html', {'username': user.username, 'ingredients': ingredients})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")

@login_required
def recipes(request, username):
    user = get_object_or_404(User, username=username)
    if admin_check(request.user) or request.user == user:
        # Placeholder for fetching recipes from the database
        recipes = []  # Replace with actual query to get recipes
        return render(request, 'products/recipes.html', {'username': user.username, 'recipes': recipes})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")

@login_required
def materials(request, username):
    user = get_object_or_404(User, username=username)
    if admin_check(request.user) or request.user == user:
        # Placeholder for fetching materials from the database
        materials = []  # Replace with actual query to get materials
        return render(request, 'products/materials.html', {'username': user.username, 'materials': materials})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")

@login_required
def packages(request, username):
    user = get_object_or_404(User, username=username)
    if admin_check(request.user) or request.user == user:
        # Placeholder for fetching packages from the database
        packages = []  # Replace with actual query to get packages
        return render(request, 'products/packages.html', {'username': user.username, 'packages': packages})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")

#customers views
@login_required
def customers(request, username):
    user = get_object_or_404(User, username=username)
    if admin_check(request.user) or request.user == user:
        # Placeholder for fetching customers from the database
        customers = []  # Replace with actual query to get customers
        return render(request, 'customers.html', {'username': user.username, 'customers': customers})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")

#expenses vierws  
@login_required
def labor_costs(request, username):
    user = get_object_or_404(User, username=username)
    if admin_check(request.user) or request.user == user:
        return render(request, 'expenses/labor_costs.html', {'username': user.username})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")

@login_required
def fixed_expenses(request, username):
    user = get_object_or_404(User, username=username)
    if admin_check(request.user) or request.user == user:
        return render(request, 'expenses/fixed_expenses.html', {'username': user.username})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")

@login_required
def variable_expenses(request, username):
    user = get_object_or_404(User, username=username)
    if admin_check(request.user) or request.user == user:
        return render(request, 'expenses/variable_expenses.html', {'username': user.username})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")

#reoports views
@login_required
def expense_report(request, username):
    user = get_object_or_404(User, username=username)
    if admin_check(request.user) or request.user == user:
        return render(request, 'reports/expense_report.html', {'username': user.username})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")

@login_required
def sales_report(request, username):
    user = get_object_or_404(User, username=username)
    if admin_check(request.user) or request.user == user:
        return render(request, 'reports/sales_report.html', {'username': user.username})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")

@login_required
def financial_overview(request, username):
    user = get_object_or_404(User, username=username)
    if admin_check(request.user) or request.user == user:
        return render(request, 'reports/financial_overview.html', {'username': user.username})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")

#configuration views   
@login_required
def configuration(request, username):
    user = get_object_or_404(User, username=username)
    if admin_check(request.user) or request.user == user:
        return render(request, 'configuration.html', {'username': user.username})
    else:
        return HttpResponseForbidden("You are not allowed to view this page.")