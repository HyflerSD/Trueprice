from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

class CarCalculatorModel(models.Model):
    car_name = models.CharField(
        max_length=40)
    car_price = models.IntegerField(
        default=0
    )
    tax_rate = models.DecimalField(
        default=0,
        decimal_places=1,
        max_digits=9,
        )
    down_payment = models.IntegerField(
        default=0
    )
    interest_rate = models.DecimalField(
        default=0,
        decimal_places=2,
        max_digits=9,
)
    loan_term_in_years = models.IntegerField(
        default=0,
    )
    trade_in_value = models.IntegerField()
    def __str__(self):
        return self.car_name