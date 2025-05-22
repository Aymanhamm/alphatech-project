from django.db import models
from employees.models import Employee

class Tache(models.Model):
    STATUT_CHOICES = [
        ('en_attente', 'En attente'),
        ('en_cours', 'En cours'),
        ('terminee', 'Terminée'),
        ('annulee', 'Annulée'),
    ]
    
    PRIORITE_CHOICES = [
        ('basse', 'Basse'),
        ('moyenne', 'Moyenne'),
        ('haute', 'Haute'),
        ('urgente', 'Urgente'),
    ]
    
    titre = models.CharField(max_length=200)
    description = models.TextField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='taches')
    attribuee_par = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='taches_attribuees')
    priorite = models.CharField(max_length=20, choices=PRIORITE_CHOICES, default='moyenne')
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')
    date_echeance = models.DateField()
    date_completion = models.DateField(null=True, blank=True)
    note_evaluation = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    commentaire_evaluation = models.TextField(blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.titre} - {self.employee.nom}"

class SoldeConge(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    solde_initial = models.IntegerField(default=0)
    jours_pris = models.IntegerField(default=0)
    jours_restants = models.IntegerField(default=0)
    solde_reporte = models.IntegerField(default=0)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Solde congés - {self.employee.nom}"