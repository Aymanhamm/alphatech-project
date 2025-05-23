from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext as _
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, _('Votre compte a été créé avec succès !'))
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, _('Vous êtes maintenant connecté.'))
            return redirect('dashboard')
        else:
            messages.error(request, _('Nom d'utilisateur ou mot de passe incorrect.'))
    return render(request, 'users/login.html')

@login_required
def home_view(request):
    """Home view that displays a welcome message and user information"""
    context = {
        'user': request.user,
        'title': _('Accueil')
    }
    return render(request, 'users/home.html', context)

@login_required
def logout_view(request):
    """Logout view that logs out the user and redirects to login page"""
    logout(request)
    messages.success(request, _('Vous êtes maintenant déconnecté.'))
    return redirect('login')

# Note: The logout functionality is now handled by logout_view

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, _('Votre profil a été mis à jour avec succès.'))
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
