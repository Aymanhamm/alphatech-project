from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Employee, Departement, Poste, Contrat, HistoriqueCarriere, Utilisateur, JournalActivite

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Type utilisateur', {'fields': ('user_type',)}),
    )
    list_display = ['username', 'email', 'user_type', 'is_staff', 'is_active']
    list_filter = ['user_type', 'is_staff', 'is_active']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['matricule', 'nom', 'prenom', 'departement', 'poste', 'date_embauche']
    list_filter = ['departement', 'poste', 'date_embauche']
    search_fields = ['matricule', 'nom', 'prenom', 'email']
    ordering = ['-date_creation']

@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    list_display = ['nom', 'description', 'date_creation']
    search_fields = ['nom']

@admin.register(Poste)
class PosteAdmin(admin.ModelAdmin):
    list_display = ['titre', 'niveau', 'date_creation']
    list_filter = ['niveau']
    search_fields = ['titre']

@admin.register(Contrat)
class ContratAdmin(admin.ModelAdmin):
    list_display = ['employee', 'type_contrat', 'date_debut', 'date_fin', 'statut']
    list_filter = ['type_contrat', 'statut']
    search_fields = ['employee__nom', 'employee__prenom']

@admin.register(HistoriqueCarriere)
class HistoriqueCarriereAdmin(admin.ModelAdmin):
    list_display = ['employee', 'type_changement', 'date_effet', 'nouveau_poste']
    list_filter = ['type_changement', 'date_effet']
    search_fields = ['employee__nom', 'employee__prenom']

@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ['nom_utilisateur', 'employee', 'actif', 'derniere_connexion']
    list_filter = ['actif']
    search_fields = ['nom_utilisateur', 'employee__nom']

@admin.register(JournalActivite)
class JournalActiviteAdmin(admin.ModelAdmin):
    list_display = ['employee', 'type_action', 'date_creation']
    list_filter = ['type_action', 'date_creation']
    search_fields = ['employee__nom', 'description']
    readonly_fields = ['date_creation']