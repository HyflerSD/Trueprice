from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, CarCalculatorModel
from .forms import CustomUserCreationForm, CustomUserChangeForm
# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    # model = CustomUser
    list_display = ['email', 'username', 'is_staff']

class SavedForm(UserAdmin):
    model = CustomUser
    list_display = ['username']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CarCalculatorModel)