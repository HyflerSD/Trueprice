# Generated by Django 3.0.8 on 2020-08-13 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20200813_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='carcalculatormodel',
            name='interest_rate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
        migrations.AddField(
            model_name='carcalculatormodel',
            name='tax_rate',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='carcalculatormodel',
            name='car_name',
            field=models.CharField(default=0, max_length=40),
        ),
        migrations.AlterField(
            model_name='carcalculatormodel',
            name='car_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='carcalculatormodel',
            name='down_payment',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='carcalculatormodel',
            name='loan_term_in_years',
            field=models.IntegerField(default=0),
        ),
    ]
