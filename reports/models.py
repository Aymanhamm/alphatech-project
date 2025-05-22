from django.db import models
from employees.models import Employee
from datetime import datetime

class Report(models.Model):
    TYPE_RAPPORT_CHOICES = [
        ('presence', 'Présences'),
        ('performance', 'Performance'),
        ('paie', 'Paie'),
        ('conge', 'Congés'),
        ('tache', 'Tâches'),
        ('recrutement', 'Recrutement'),
    ]
    
    FORMAT_CHOICES = [
        ('pdf', 'PDF'),
        ('excel', 'Excel'),
        ('csv', 'CSV'),
        ('html', 'HTML'),
    ]
    
    titre = models.CharField(max_length=200)
    type_rapport = models.CharField(max_length=20, choices=TYPE_RAPPORT_CHOICES)
    format = models.CharField(max_length=10, choices=FORMAT_CHOICES, default='pdf')
    periode_debut = models.DateField()
    periode_fin = models.DateField()
    chemin_fichier = models.FileField(upload_to='rapports/')
    generate_par = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='rapports_generes')
    date_generation = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.titre} - {self.get_type_rapport_display()}"
    
    def save(self, *args, **kwargs):
        # Format the file name
        if not self.chemin_fichier:
            self.chemin_fichier = f"rapports/{self.titre.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.{self.format}"
        
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Rapport'
        verbose_name_plural = 'Rapports'
        ordering = ['-date_generation']
