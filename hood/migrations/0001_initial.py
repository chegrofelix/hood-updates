# Generated by Django 3.2 on 2021-04-13 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hoodName', models.CharField(max_length=100)),
                ('hoodLocation', models.CharField(max_length=50, null=True)),
                ('occupantsCount', models.PositiveSmallIntegerField(null=True)),
                ('admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Social_Ammenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ammenityName', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('hood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hood.hood')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_confirmed', models.BooleanField(default=False)),
                ('idNumber', models.CharField(max_length=500, null=True, unique=True)),
                ('name', models.CharField(blank=True, max_length=500)),
                ('avatar', models.ImageField(upload_to='profilepic/')),
                ('generalLocation', models.TextField(blank=True, max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('hood', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hood.hood')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=2000)),
                ('postDate', models.DateTimeField(auto_now_add=True)),
                ('hood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hood.hood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-postDate'],
            },
        ),
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hood_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hood.hood')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=100, null=True)),
                ('description_of_biz', models.TextField(null=True)),
                ('location', models.CharField(max_length=1000, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('hood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hood.hood')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]