from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    USER_TYPE_CHOICES = [
        ('employee', _('Employé')),
        ('admin', _('Administrateur')),
        ('project_manager', _('Chef de Projet')),
        ('hr_manager', _('Gestionnaire RH')),
    ]
    
    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
        default='employee',
        verbose_name=_('Type d'utilisateur')
    )
    
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        verbose_name=_('Numéro de téléphone')
    )
    
    date_of_birth = models.DateField(
        null=True,
        blank=True,
        verbose_name=_('Date de naissance')
    )
    
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        null=True,
        blank=True,
        verbose_name=_('Photo de profil')
    )
    
    class Meta:
        verbose_name = _('Utilisateur')
        verbose_name_plural = _('Utilisateurs')
        
    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"
    
    def is_hr(self):
        """Check if user is HR manager or admin"""
        return self.user_type in ['hr_manager', 'admin']
    
    def is_manager(self):
        """Check if user is project manager or admin"""
        return self.user_type in ['project_manager', 'admin']
    
    def get_full_name(self):
        """Return the full name of the user"""
        return f"{self.first_name} {self.last_name}" if self.first_name and self.last_name else self.username
    
    def get_short_name(self):
        """Return the short name of the user"""
        return self.first_name or self.username