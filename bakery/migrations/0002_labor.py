# Generated by Django 5.0.6 on 2024-06-27 01:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Labor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('daily_hours', models.FloatField()),
                ('days_worked', models.IntegerField()),
                ('monthly_wage', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bakery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='labor', to='bakery.bakery')),
            ],
        ),
    ]
