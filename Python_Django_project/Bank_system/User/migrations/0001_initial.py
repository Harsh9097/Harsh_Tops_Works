# Generated by Django 4.2.2 on 2023-07-07 04:53

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('role', models.CharField(blank=True, choices=[('Manager', 'Manager'), ('Staff', 'Staff'), ('Customer', 'Customer')], max_length=20, null=True)),
                ('contact_number', models.BigIntegerField(blank=True, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='0', max_length=30)),
                ('adhar_no', models.BigIntegerField(blank=True, null=True)),
                ('pan_no', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.TextField(blank=True, max_length=50, null=True)),
                ('profile', models.ImageField(upload_to='media/profile/')),
                ('father_name', models.CharField(blank=True, max_length=50, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=50, null=True)),
                ('nationality', models.CharField(blank=True, max_length=50, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('marital_status', models.CharField(blank=True, choices=[('Married', 'Married'), ('Unmarried', 'Unmarried')], max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('accounts_type', models.CharField(choices=[('Saving Account', 'Saving Account'), ('Current Account', 'Current Account'), ('Personal Account', 'Personal Account'), ('Recurring Deposit', 'Recurring Deposit'), ('Fixed Deposit Account', 'Fixed Deposit Account')], max_length=30)),
                ('account_no', models.BigIntegerField()),
                ('balance', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('security_pin', models.IntegerField(blank=True, default=None, null=True)),
                ('is_first_account', models.BooleanField(default=False)),
                ('is_approve', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_account', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]