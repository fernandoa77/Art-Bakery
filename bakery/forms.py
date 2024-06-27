from django import forms
from .models import Ingredient, Material

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'unit', 'cost']


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name', 'quantity', 'unit', 'cost']
