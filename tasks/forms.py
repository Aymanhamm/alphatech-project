from django import forms
from .models import Tache
from employees.models import Employee

class TacheForm(forms.ModelForm):
    class Meta:
        model = Tache
        fields = ['titre', 'description', 'employee', 'priorite', 'date_echeance']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'employee': forms.Select(attrs={'class': 'form-control'}),
            'priorite': forms.Select(attrs={'class': 'form-control'}),
            'date_echeance': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class TacheEvaluationForm(forms.ModelForm):
    class Meta:
        model = Tache
        fields = ['statut', 'note_evaluation', 'commentaire_evaluation']
        widgets = {
            'statut': forms.Select(attrs={'class': 'form-control'}),
            'note_evaluation': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0', 'max': '10'}),
            'commentaire_evaluation': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }