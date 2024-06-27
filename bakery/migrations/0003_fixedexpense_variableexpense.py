# Generated by Django 5.0.6 on 2024-06-27 03:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0002_labor'),
    ]

    operations = [
        migrations.CreateModel(
            name='FixedExpense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concept', models.CharField(max_length=100)),
                ('monthly_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bakery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fixed_expenses', to='bakery.bakery')),
            ],
        ),
        migrations.CreateModel(
            name='VariableExpense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concept', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bakery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variable_expenses', to='bakery.bakery')),
            ],
        ),
    ]
