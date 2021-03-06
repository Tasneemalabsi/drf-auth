from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import UserCreationForm

class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    model = CustomUser
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = ((None,{'fields':('username', 'email', 'first_name', 'last_name', 'password')}),)

# Register your models here.
admin.site.register(CustomUser, UserAdmin)
