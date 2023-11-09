# Generated by Django 4.2.2 on 2023-07-07 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='from_account_number',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='to_account_number',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]