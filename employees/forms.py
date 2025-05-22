from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Employee, Contrat, Departement, Poste
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nom d\'utilisateur'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Mot de passe'
        })
    )

class EmployeeForm(forms.ModelForm):
    username = forms.CharField(max_length=150, label="Nom d'utilisateur")
    password = forms.CharField(widget=forms.PasswordInput(), label="Mot de passe")
    user_type = forms.ChoiceField(choices=User.USER_TYPE_CHOICES, label="Type d'utilisateur")
    
    class Meta:
        model = Employee
        fields = ['matricule', 'prenom', 'nom', 'date_naissance', 'adresse', 
                 'email', 'telephone', 'date_embauche', 'departement', 'poste', 'superviseur']
        widgets = {
            'date_naissance': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'date_embauche': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'matricule': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'adresse': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'departement': forms.Select(attrs={'class': 'form-control'}),
            'poste': forms.Select(attrs={'class': 'form-control'}),
            'superviseur': forms.Select(attrs={'class': 'form-control'}),
        }

class ContratForm(forms.ModelForm):
    class Meta:
        model = Contrat
        fields = ['employee', 'type_contrat', 'date_debut', 'date_fin', 
                 'salaire_base', 'statut', 'chemin_document']
        widgets = {
            'date_debut': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'date_fin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'employee': forms.Select(attrs={'class': 'form-control'}),
            'type_contrat': forms.Select(attrs={'class': 'form-control'}),
            'salaire_base': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'statut': forms.Select(attrs={'class': 'form-control'}),
            'chemin_document': forms.FileInput(attrs={'class': 'form-control'}),
        }

class DepartementForm(forms.ModelForm):
    class Meta:
        model = Departement
        fields = ['nom', 'description']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class PosteForm(forms.ModelForm):
    class Meta:
        model = Poste
        fields = ['titre', 'description', 'niveau']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'niveau': forms.NumberInput(attrs={'class': 'form-control'}),
        }    