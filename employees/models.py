from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()

class Departement(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nom

class Poste(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    niveau = models.IntegerField(default=1)
    date_creation = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titre

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricule = models.CharField(max_length=20, unique=True)
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    date_naissance = models.DateField()
    adresse = models.TextField()
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    date_embauche = models.DateField()
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    poste = models.ForeignKey(Poste, on_delete=models.CASCADE)
    superviseur = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.matricule})"

class Contrat(models.Model):
    TYPE_CONTRAT_CHOICES = [
        ('CDI', 'CDI'),
        ('CDD', 'CDD'),
        ('Interim', 'Intérim'),
        ('Stage', 'Stage'),
    ]
    STATUT_CHOICES = [
        ('active', 'Actif'),
        ('expire', 'Expiré'),
        ('resilie', 'Résilié'),
    ]
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    type_contrat = models.CharField(max_length=20, choices=TYPE_CONTRAT_CHOICES)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    salaire_base = models.DecimalField(max_digits=10, decimal_places=2)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='active')
    chemin_document = models.FileField(upload_to='contracts/')
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Contrat {self.type_contrat} - {self.employee.nom}"

class HistoriqueCarriere(models.Model):
    TYPE_CHANGEMENT_CHOICES = [
        ('promotion', 'Promotion'),
        ('mutation', 'Mutation'),
        ('augmentation', 'Augmentation'),
    ]
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    type_changement = models.CharField(max_length=20, choices=TYPE_CHANGEMENT_CHOICES)
    date_effet = models.DateField()
    description = models.TextField()
    ancien_poste = models.CharField(max_length=100, blank=True)
    nouveau_poste = models.CharField(max_length=100, blank=True)
    ancien_salaire = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    nouveau_salaire = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    chemin_document = models.FileField(upload_to='career_history/', blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.type_changement} - {self.employee.nom} ({self.date_effet})"

class JournalActivite(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    type_action = models.CharField(max_length=50)
    description = models.TextField()
    adresse_ip = models.GenericIPAddressField()
    date_creation = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.type_action} - {self.employee.nom} ({self.date_creation})"