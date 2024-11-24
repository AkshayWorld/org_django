from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Organization, CustomUser, Role
from .forms import UserForm, RoleAssignmentForm
from django import forms
from .forms import OrganizationForm
@login_required
def organization_list(request):
    if not request.user.organization: #or not request.user.organization .is_main:
        return redirect("user_list")
    organizations = Organization.objects.all()
    return render(request, "org_list.html", {"organizations": organizations})

@login_required
def organization_create(request):
    if not request.user.organization:# or not request.user.organization.is_main:
        return redirect("user_list")
    if request.method == "POST":
        A = OrganizationForm(request.POST)
        if A.is_valid():
            A.save()
            return redirect("organization_list")
    else:
        A = OrganizationForm()
    return render(request, "org_create.html", {"form": A})

@login_required
def user_list(request):
    users = CustomUser.objects.filter(organization=request.user.organization)
    return render(request, "user_list.html", {"users": users})

@login_required
def user_create(request):
    if not request.user.is_staff:
        return redirect("user_list")
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user_list")
    else:
        form = UserForm()
    return render(request, "user_create.html", {"form": form})

@login_required
def assign_role(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id, organization=request.user.organization)
    if not request.user.is_staff:
        return redirect("user_list")
    if request.method == "POST":
        form = RoleAssignmentForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("user_list")
    else:
        form = RoleAssignmentForm(instance=user)
    return render(request, "assign_role.html", {"form": form, "user": user})
