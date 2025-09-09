from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'name', 'is_staff', 'is_active')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email','password')}),
        ('Personal', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_staff','is_active','is_superuser','groups','user_permissions')}),
    )
    add_fieldsets = (
        (None, {'classes':('wide',),'fields':('email','name','password1','password2','is_staff','is_active')}),
    )
