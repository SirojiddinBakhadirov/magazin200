# Generated by Django 4.1.1 on 2022-09-19 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='vozvrat',
        ),
    ]