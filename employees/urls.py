from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_view, name='employee_profile'),
    path('list/', views.employee_list, name='employee_list'),
    path('<int:employee_id>/', views.employee_detail, name='employee_detail'),
    path('create/', views.employee_create, name='employee_create'),
    path('<int:employee_id>/edit/', views.employee_edit, name='employee_edit'),
    path('contrats/', views.contrat_list, name='contrat_list'),
    path('contrats/create/', views.contrat_create, name='contrat_create'),
    path('departements/', views.departement_list, name='departement_list'),
    path('departements/create/', views.departement_create, name='departement_create'),
    path('postes/', views.poste_list, name='poste_list'),
    path('postes/create/', views.poste_create, name='poste_create'),
]