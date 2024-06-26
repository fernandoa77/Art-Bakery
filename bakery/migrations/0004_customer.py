# Generated by Django 5.0.6 on 2024-06-27 16:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0003_fixedexpense_variableexpense'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('origin', models.CharField(max_length=100)),
                ('bakery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='bakery.bakery')),
            ],
        ),
    ]
