# Generated by Django 3.2 on 2022-09-23 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='author',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='authors.author'),
        ),
    ]
