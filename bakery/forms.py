from django import forms
from .models import Ingredient, Material, Labor, FixedExpense, VariableExpense, Customer
from bootstrap_datepicker_plus.widgets import DatePickerInput

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'unit', 'cost']


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name', 'quantity', 'unit', 'cost']


class LaborForm(forms.ModelForm):
    class Meta:
        model = Labor
        fields = ['name', 'daily_hours', 'days_worked', 'monthly_wage']




class FixedExpenseForm(forms.ModelForm):
    class Meta:
        model = FixedExpense
        fields = ['concept', 'monthly_cost']


class VariableExpenseForm(forms.ModelForm):
    class Meta:
        model = VariableExpense
        fields = ['concept', 'date', 'amount']
        widgets = {
            'date': DatePickerInput(format='%Y-%m-%d'),
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'address', 'phone', 'email', 'origin']