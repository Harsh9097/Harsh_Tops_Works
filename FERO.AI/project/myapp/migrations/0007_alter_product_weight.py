# Generated by Django 5.0 on 2023-12-06 08:07

import myapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=5, validators=[myapp.models.validate_weight]),
        ),
    ]
