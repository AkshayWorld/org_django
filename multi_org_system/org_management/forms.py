from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Role, Organization

class UserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "organization", "role", "password1", "password2"]

class RoleAssignmentForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["role"]


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'address',"is_main"]  
