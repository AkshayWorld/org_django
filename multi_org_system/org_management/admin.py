from django.contrib import admin
# Register your models here.
from .models import Organization, Role, CustomUser

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "is_main")
    list_filter = ("is_main",)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "organization", "role", "is_staff")
    list_filter = ("organization", "role")
