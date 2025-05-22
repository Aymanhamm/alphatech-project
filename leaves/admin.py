from django.contrib import admin
from .models import Conge

@admin.register(Conge)
class CongeAdmin(admin.ModelAdmin):
    list_display = ['employee', 'type_conge', 'date_debut', 'date_fin', 'jours_total', 'statut']
    list_filter = ['type_conge', 'statut', 'date_debut']
    search_fields = ['employee__nom', 'employee__prenom']
    readonly_fields = ['jours_total', 'date_creation', 'date_modification']
    ordering = ['-date_creation']