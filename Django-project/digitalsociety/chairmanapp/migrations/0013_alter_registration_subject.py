# Generated by Django 4.1.6 on 2023-02-24 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chairmanapp', '0012_alter_registration_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='subject',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
