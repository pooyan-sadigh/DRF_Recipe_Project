from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext as _

from .models import Account


class AccountAdmin(UserAdmin):
    """creates our account admin page"""

    ordering = ['id']
    list_display = ['email', 'username', 'is_superuser']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Account Info'), {'fields': ('username',)}),
        (
            _('Account Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Dates'), {'fields': ('last_login', 'timestamp')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )


admin.site.register(Account, AccountAdmin)
