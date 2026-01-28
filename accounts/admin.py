from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .forms import UserChangeForm, UserCreationsForm
from .models import User


class UserAmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationsForm

    list_display = ('email', 'phone_number', 'is_admin')
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields': ('email', 'phone_number', 'full_name', 'password')}),
        ('permissions', {'fields': ('is_active', 'is_admin', 'last_login')}),
    )

    add_fieldsets = (
        (None, {'fields':('phone_number', 'email', 'full_name', 'password1', 'password2')}),
    )

    search_fields = ('email', 'full_name')
    ordering = ('email',)
    filter_horizontal = ()

admin.site.unregister(Group)
admin.site.register(User, UserAmin)



