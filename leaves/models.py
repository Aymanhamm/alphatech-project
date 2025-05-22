from django.db import models
from employees.models import Employee

class SoldeConge(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='solde_conges')
    annee = models.IntegerField()
    solde_initial = models.DecimalField(max_digits=5, decimal_places=1)
    jours_pris = models.DecimalField(max_digits=5, decimal_places=1, default=0)
    jours_restants = models.DecimalField(max_digits=5, decimal_places=1)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Solde {self.annee} - {self.employee.nom}"
    
    def save(self, *args, **kwargs):
        # Calculate remaining days
        self.jours_restants = self.solde_initial - self.jours_pris
        super().save(*args, **kwargs)

class Conge(models.Model):
    TYPE_CONGE_CHOICES = [
        ('annuel', 'Congé annuel'),
        ('maladie', 'Congé maladie'),
        ('maternite', 'Congé maternité'),
        ('paternite', 'Congé paternité'),
        ('exceptionnel', 'Congé exceptionnel'),
        ('sans_solde', 'Congé sans solde'),
    ]
    
    STATUT_CHOICES = [
        ('en_attente', 'En attente'),
        ('approuve', 'Approuvé'),
        ('refuse', 'Refusé'),
        ('annule', 'Annulé'),
    ]
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='conges')
    type_conge = models.CharField(max_length=20, choices=TYPE_CONGE_CHOICES)
    date_debut = models.DateField()
    date_fin = models.DateField()
    jours_total = models.IntegerField()
    motif = models.TextField(blank=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')
    approuve_par = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='conges_approuves')
    commentaire_approbation = models.TextField(blank=True)
    date_approbation = models.DateTimeField(null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.get_type_conge_display()} - {self.employee.nom} ({self.date_debut} - {self.date_fin})"

    def save(self, *args, **kwargs):
        # Calculate total days
        if self.date_debut and self.date_fin:
            delta = self.date_fin - self.date_debut
            self.jours_total = delta.days + 1
            
            # Update leave balance if it's an annual leave
            if self.type_conge == 'annuel' and self.statut == 'approuve':
                current_year = self.date_debut.year
                solde = SoldeConge.objects.filter(employee=self.employee, annee=current_year).first()
                if solde:
                    solde.jours_pris += self.jours_total
                    solde.save()
        
        super().save(*args, **kwargs)