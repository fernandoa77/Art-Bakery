from django import forms
from .models import Ingredient, Material, Labor

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
