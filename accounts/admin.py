from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import CustomUser, CustomUserProfile
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserProfileInline(admin.StackedInline):
    model = CustomUserProfile
    can_delete = False
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display_links = ['email']
    search_fields = ('email',)
    ordering = ('email',)
    list_display = ('email', 'is_staff', 'is_active', 'is_superuser',)
    list_filter = ('email', 'is_staff', 'is_active', 'is_superuser',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login',)}),
        )


admin.site.register(CustomUser, CustomUserAdmin)