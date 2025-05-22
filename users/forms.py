from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _
from .models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=20, required=False)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name',
                  'phone_number', 'user_type')
        labels = {
            'username': _('Nom d\'utilisateur'),
            'email': _('Email'),
            'password1': _('Mot de passe'),
            'password2': _('Confirmation du mot de passe'),
            'first_name': _('Prénom'),
            'last_name': _('Nom'),
            'phone_number': _('Numéro de téléphone'),
            'user_type': _('Type d\'utilisateur')
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'phone_number', 'user_type')
        labels = {
            'username': _('Nom d\'utilisateur'),
            'email': _('Email'),
            'first_name': _('Prénom'),
            'last_name': _('Nom'),
            'phone_number': _('Numéro de téléphone'),
            'user_type': _('Type d\'utilisateur')
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('profile_picture', 'date_of_birth')
        labels = {
            'profile_picture': _('Photo de profil'),
            'date_of_birth': _('Date de naissance')
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
