# Generated by Django 3.0.8 on 2020-07-25 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200725_0125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='age',
        ),
    ]
