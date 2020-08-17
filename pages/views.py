from __future__ import unicode_literals

from django.views.generic import TemplateView
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import CarCalculatorForm, FeedBackForm

from amortization.amount import calculate_amortization_amount
from amortization.schedule import amortization_schedule
from tabulate import tabulate

class HomePageView(TemplateView):
    template_name = 'index.html'

    #Calculator form functionallity
    def get(self, request, *args, **kwargs):
        form = CarCalculatorForm
        return render(request, 'index.html', {'form': form})

    def post(self, request):
        form = CarCalculatorForm(request.POST)
        if form.is_valid():
            form.save()
            car_price = form.cleaned_data["car_price"]
            tax_rate = float(form.cleaned_data["tax_rate"])
            downpayment = form.cleaned_data["down_payment"]
            loan_term = form.cleaned_data["loan_term_in_years"]
            apr = float(form.cleaned_data["interest_rate"])
            trade_value = form.cleaned_data["trade_in_value"]
            # if use
            
            if 'calc' in request.POST:
                loan_amount = int(((tax_rate*0.01) * (car_price)) + car_price) - (downpayment + trade_value)
                interest = ((apr * 0.01)/12)
                total_interest_amount = "{:.0f}".format((interest) * (loan_amount))
                monthly = ((loan_amount * interest)*((1 + interest)**(12*loan_term)))/ (((1 + interest)**(12*loan_term)) -1)
                monthly_payment = "{:.2f}".format(monthly)




                table = (amortization_schedule(loan_amount, interest, loan_term*12))
                print(
                    tabulate(
                        table,
                        headers=["Payments", "Amount", "Interest", "Principal", "Balance"],
                        floatfmt=",.2f",
                        numalign="right"
                    )
                )               
            
            # form = CarCalculatorForm
        else:
            def sendform(self, request):
                getdata = self.get_context_data(post)
        args= {
            'form': form, 'loan_amount': loan_amount, 'monthly_payment': monthly_payment,
            'interest': interest, 'total_interest_amount': total_interest_amount,
            'table': table}
        return render(request, 'index.html', args)

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'


class FeedBackPageView(TemplateView):
    #Calculator form functionallity
    def get(self, request):
        form = FeedBackForm
        return render(request, 'pages/feedback.html', {'form': form})

    def post(self, request):
        form = FeedBackForm(request.POST)
        name = form.cleaned_data["name"]
        email = form.changed_data["email"]
        comment = form.cleaned_data["comment"]
        if form.is_valid():
            return render(request, 'index.html')

            form = FeedBackForm
        else:
            form = FeedBackForm()
            # def sendform(self, request):
            # getdata = self.get_context_data(post)
            args= {
                'form': form}
        return render(request, 'pages/feedback.html', args)
    template_name = 'pages/feedback.html'
class BlogPageView(TemplateView):
    template_name = 'pages/blog.html'