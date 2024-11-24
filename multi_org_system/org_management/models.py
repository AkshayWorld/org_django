from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

class Organization(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    organization = models.ForeignKey(
        "Organization", on_delete=models.CASCADE, related_name="users", null=True, blank=True
    )
    role = models.ForeignKey(
        "Role", on_delete=models.SET_NULL, related_name="users", null=True, blank=True
    )

    # Add unique related_name attributes to avoid conflicts
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # Custom related_name
        verbose_name=_("groups"),
        blank=True,
        help_text=_("The groups this user belongs to."),
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_set_permissions",  # Custom related_name
        verbose_name=_("user permissions"),
        blank=True,
        help_text=_("Specific permissions for this user."),
    )