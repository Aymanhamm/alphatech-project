from django.db import models
from employees.models import Employee
from datetime import datetime

class Paie(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='paies')
    mois_periode = models.CharField(max_length=20)
    annee_periode = models.IntegerField()
    salaire_base = models.DecimalField(max_digits=10, decimal_places=2)
    primes = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    salaire_net = models.DecimalField(max_digits=10, decimal_places=2)
    date_paiement = models.DateField()
    chemin_bulletin = models.FileField(upload_to='bulletins_paie/')
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.employee.nom} - {self.mois_periode} {self.annee_periode}"
    
    def save(self, *args, **kwargs):
        # Calculate net salary
        self.salaire_net = self.salaire_base + self.primes - self.deductions
        
        # Format month name
        if not self.mois_periode:
            self.mois_periode = datetime.now().strftime('%B')
        
        super().save(*args, **kwargs)
    
    class Meta:
        unique_together = ('employee', 'mois_periode', 'annee_periode')
        verbose_name = 'Bulletin de paie'
        verbose_name_plural = 'Bulletins de paie'
