from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'phone_number', 'is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('phone_number',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('phone_number',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
