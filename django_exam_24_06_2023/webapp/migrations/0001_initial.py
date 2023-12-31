# Generated by Django 4.2.2 on 2023-06-24 07:00

import django.core.validators
from django.db import migrations, models
import django_exam_24_06_2023.webapp.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), django_exam_24_06_2023.webapp.validators.validate_letters_only], verbose_name='Name')),
                ('image_url', models.URLField(verbose_name='Image URL')),
                ('description', models.TextField(verbose_name='Description')),
                ('nutrition', models.TextField(blank=True, null=True, verbose_name='Nutrition')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, validators=[django.core.validators.MinLengthValidator(2), django_exam_24_06_2023.webapp.validators.validate_first_char_is_letter], verbose_name='First Name')),
                ('last_name', models.CharField(max_length=35, validators=[django.core.validators.MinLengthValidator(1), django_exam_24_06_2023.webapp.validators.validate_first_char_is_letter], verbose_name='Last Name')),
                ('email', models.EmailField(max_length=40, verbose_name='Email')),
                ('password', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(8)], verbose_name='Password')),
                ('image_url', models.URLField(blank=True, null=True, verbose_name='Image URL')),
                ('age', models.IntegerField(blank=True, default=18, null=True, verbose_name='Age')),
            ],
        ),
    ]
