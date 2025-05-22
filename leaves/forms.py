from django import forms
from .models import Conge
from datetime import date

class CongeForm(forms.ModelForm):
    class Meta:
        model = Conge
        fields = ['type_conge', 'date_debut', 'date_fin', 'motif']
        widgets = {
            'type_conge': forms.Select(attrs={'class': 'form-control'}),
            'date_debut': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'date_fin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'motif': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

    def clean(self):
        cleaned_data = super().clean()
        date_debut = cleaned_data.get('date_debut')
        date_fin = cleaned_data.get('date_fin')

        if date_debut and date_fin:
            if date_debut < date.today():
                raise forms.ValidationError("La date de début ne peut pas être dans le passé.")
            if date_fin < date_debut:
                raise forms.ValidationError("La date de fin doit être postérieure à la date de début.")

        return cleaned_data

class CongeApprovalForm(forms.ModelForm):
    class Meta:
        model = Conge
        fields = ['statut', 'commentaire_approbation']
        widgets = {
            'statut': forms.Select(attrs={'class': 'form-control'}),
            'commentaire_approbation': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Limit status choices for approval
        self.fields['statut'].choices = [
            ('approuve', 'Approuvé'),
            ('refuse', 'Refusé'),
        ]