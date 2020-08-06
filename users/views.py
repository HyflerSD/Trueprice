from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import TemplateView
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'
