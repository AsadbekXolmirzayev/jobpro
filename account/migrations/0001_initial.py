# Generated by Django 4.2.1 on 2023-05-13 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=225)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.country')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(db_index=True, max_length=60, unique=True, verbose_name='Username')),
                ('first_name', models.CharField(max_length=60, null=True, verbose_name='First name')),
                ('last_name', models.CharField(max_length=60, null=True, verbose_name='Last name')),
                ('avatar', models.ImageField(upload_to='account/')),
                ('bio', models.TextField()),
                ('role', models.IntegerField(choices=[(0, 'HR'), (1, 'Candidate'), (2, 'Admin')], default=0)),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Super user')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff user')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active user')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.city')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.company')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
