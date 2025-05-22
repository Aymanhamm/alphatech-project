from django.contrib import admin
from .models import Tache, SoldeConge

@admin.register(Tache)
class TacheAdmin(admin.ModelAdmin):
    list_display = ['titre', 'employee', 'attribuee_par', 'priorite', 'statut', 'date_echeance']
    list_filter = ['priorite', 'statut', 'date_echeance']
    search_fields = ['titre', 'employee__nom', 'employee__prenom']
    ordering = ['-date_creation']

@admin.register(SoldeConge)
class SoldeCongeAdmin(admin.ModelAdmin):
    list_display = ['employee', 'solde_initial', 'jours_pris', 'jours_restants']
    search_fields = ['employee__nom', 'employee__prenom']