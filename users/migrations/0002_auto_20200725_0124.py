# Generated by Django 3.0.8 on 2020-07-25 01:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='age',
            new_name='page',
        ),
    ]
