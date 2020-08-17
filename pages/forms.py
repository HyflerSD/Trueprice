from django import forms
from django.forms import  ModelForm
from users.models import CarCalculatorModel

class CarCalculatorForm(forms.ModelForm):
    car_price = forms.IntegerField(
        label = 'Car Price',
        required=True,
        min_value=0,
        initial=10000
        )
    tax_rate = forms.DecimalField(
        label="Tax Rate %",
        required=True,min_value=0,
        decimal_places=1,
        max_digits=9,
        max_value= float(9.47),
        initial=7,
        )
    down_payment = forms.IntegerField(
        label="Down Payment",
        required=False,
        min_value=0,
        initial=2140,)
    interest_rate = forms.DecimalField(
        label="Interest Rate %",
        required=True,
        decimal_places=2,
        max_digits=9,
        min_value=0,
        max_value=25,
        initial=3.99,)
    loan_term_in_years = forms.IntegerField(
        label="Loan Term in years",
        required=True,
        min_value=1,
        max_value=15,
        initial=3,)
    trade_in_value = forms.IntegerField(
        label="Tade In Value",
        required=False,
        min_value=0,
        initial=0,
    )
    class Meta:
        model = CarCalculatorModel
        fields = '__all__'

class FeedBackForm(forms.Form):
    name = forms.CharField(
        label='Your Name',
        max_length=50)
    email = forms.EmailField(required=True)
    comment = forms.CharField(widget=forms.Textarea)

class PersonForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)