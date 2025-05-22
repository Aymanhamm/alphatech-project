from django.db import models
from employees.models import Employee

class EvaluationPerformance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='performances')
    periode_evaluation = models.CharField(max_length=50)
    objectifs_realises = models.DecimalField(max_digits=5, decimal_places=2)
    objectifs_prevus = models.DecimalField(max_digits=5, decimal_places=2)
    taux_realisation = models.DecimalField(max_digits=5, decimal_places=2)
    note_globale = models.DecimalField(max_digits=3, decimal_places=1)
    observations = models.TextField()
    evalue_par = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='evaluations_effectuees')
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Evaluation {self.periode_evaluation} - {self.employee.nom}"
    
    def save(self, *args, **kwargs):
        # Calculate realization rate
        if self.objectifs_prevus > 0:
            self.taux_realisation = (self.objectifs_realises / self.objectifs_prevus) * 100
        
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Évaluation de performance'
        verbose_name_plural = 'Évaluations de performance'
        ordering = ['-periode_evaluation']
