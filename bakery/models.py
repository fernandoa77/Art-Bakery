from django.contrib.auth.models import User
from django.db import models

class Bakery(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_bakeries')

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    bakery = models.ForeignKey(Bakery, on_delete=models.CASCADE, related_name='ingredients')
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    unit = models.CharField(max_length=10)  # e.g., mg, g, kg, etc.
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Material(models.Model):
    bakery = models.ForeignKey(Bakery, on_delete=models.CASCADE, related_name='materials')
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    unit = models.CharField(max_length=10)  # e.g., mg, g, kg, etc.
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Labor(models.Model):
    bakery = models.ForeignKey(Bakery, on_delete=models.CASCADE, related_name='labor')
    name = models.CharField(max_length=100)
    daily_hours = models.FloatField()
    days_worked = models.IntegerField()
    monthly_wage = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class FixedExpense(models.Model):
    bakery = models.ForeignKey(Bakery, on_delete=models.CASCADE, related_name='fixed_expenses')
    concept = models.CharField(max_length=100)
    monthly_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.concept

class VariableExpense(models.Model):
    bakery = models.ForeignKey(Bakery, on_delete=models.CASCADE, related_name='variable_expenses')
    concept = models.CharField(max_length=100)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.concept


class Customer(models.Model):
    bakery = models.ForeignKey(Bakery, on_delete=models.CASCADE, related_name='customers')
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    origin = models.CharField(max_length=100)

    def __str__(self):
        return self.name