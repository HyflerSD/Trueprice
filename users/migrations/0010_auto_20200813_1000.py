# Generated by Django 3.0.8 on 2020-08-13 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarCalculatorModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=40)),
                ('car_price', models.IntegerField()),
                ('down_payment', models.IntegerField()),
                ('loan_term_in_years', models.IntegerField()),
                ('trade_in_value', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
