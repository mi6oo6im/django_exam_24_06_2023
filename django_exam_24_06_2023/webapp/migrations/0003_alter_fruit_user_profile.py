# Generated by Django 4.2.2 on 2023-06-30 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_fruit_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruit',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.userprofile'),
        ),
    ]
