from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.db.models import Q
from .models import Employee, Departement, Poste
from .forms import EmployeeForm, DepartementForm, PosteForm
from datetime import datetime

@login_required
@permission_required('employees.view_employee', raise_exception=True)
def employee_list(request):
    search_query = request.GET.get('search', '')
    employees = Employee.objects.all()
    
    if search_query:
        employees = employees.filter(
            Q(prenom__icontains=search_query) |
            Q(nom__icontains=search_query) |
            Q(matricule__icontains=search_query)
        )
    
    return render(request, 'employees/employee_list.html', {
        'employees': employees,
        'search_query': search_query
    })

@login_required
@permission_required('employees.add_employee', raise_exception=True)
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.user = request.user
            employee.save()
            messages.success(request, 'Employé créé avec succès')
            return redirect('employees:employee_list')
    else:
        form = EmployeeForm()
    
    return render(request, 'employees/employee_form.html', {
        'form': form,
        'title': 'Nouvel employé'
    })

@login_required
@permission_required('employees.change_employee', raise_exception=True)
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employé mis à jour avec succès')
            return redirect('employees:employee_list')
    else:
        form = EmployeeForm(instance=employee)
    
    return render(request, 'employees/employee_form.html', {
        'form': form,
        'title': 'Modifier employé'
    })

@login_required
@permission_required('employees.delete_employee', raise_exception=True)
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    
    if request.method == 'POST':
        employee.delete()
        messages.success(request, 'Employé supprimé avec succès')
        return redirect('employees:employee_list')
    
    return render(request, 'employees/employee_confirm_delete.html', {
        'employee': employee
    })

@login_required
def employee_profile(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employees/employee_profile.html', {
        'employee': employee
    })

@login_required
@permission_required('employees.view_departement', raise_exception=True)
def departement_list(request):
    departements = Departement.objects.all()
    return render(request, 'employees/departement_list.html', {
        'departements': departements
    })

@login_required
@permission_required('employees.add_departement', raise_exception=True)
def departement_create(request):
    if request.method == 'POST':
        form = DepartementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Département créé avec succès')
            return redirect('employees:departement_list')
    else:
        form = DepartementForm()
    
    return render(request, 'employees/departement_form.html', {
        'form': form,
        'title': 'Nouveau département'
    })

@login_required
@permission_required('employees.view_poste', raise_exception=True)
def poste_list(request):
    postes = Poste.objects.all()
    return render(request, 'employees/poste_list.html', {
        'postes': postes
    })

@login_required
@permission_required('employees.add_poste', raise_exception=True)
def poste_create(request):
    if request.method == 'POST':
        form = PosteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Poste créé avec succès')
            return redirect('employees:poste_list')
    else:
        form = PosteForm()
    
    return render(request, 'employees/poste_form.html', {
        'form': form,
        'title': 'Nouveau poste'
    })

@login_required
def employee_dashboard(request):
    if request.user.is_hr:
        total_employees = Employee.objects.count()
        new_employees = Employee.objects.filter(
            date_embauche__gte=datetime.now().date() - timedelta(days=30)
        ).count()
        
        return render(request, 'employees/hr_dashboard.html', {
            'total_employees': total_employees,
            'new_employees': new_employees
        })
    else:
        return render(request, 'employees/employee_dashboard.html')
