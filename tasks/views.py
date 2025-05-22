from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.utils import timezone
from employees.models import Employee
from .models import Tache
from .forms import TacheForm, TacheEvaluationForm

@login_required
def task_list(request):
    if request.user.user_type == 'employee':
        # Employees can only see their own tasks
        try:
            employee = Employee.objects.get(user=request.user)
            tasks = Tache.objects.filter(employee=employee).order_by('-date_creation')
        except Employee.DoesNotExist:
            messages.error(request, 'Profil employé non trouvé.')
            return redirect('home')
    else:
        # Admins and project managers can see all tasks
        tasks = Tache.objects.all().order_by('-date_creation')
    
    # Filter by status if provided
    status_filter = request.GET.get('status')
    if status_filter:
        tasks = tasks.filter(statut=status_filter)
    
    paginator = Paginator(tasks, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'tasks/task_list.html', {
        'page_obj': page_obj,
        'status_filter': status_filter,
        'status_choices': Tache.STATUT_CHOICES
    })

@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Tache, id=task_id)
    
    # Check permissions
    if request.user.user_type == 'employee':
        try:
            employee = Employee.objects.get(user=request.user)
            if task.employee != employee:
                messages.error(request, 'Accès non autorisé.')
                return redirect('task_list')
        except Employee.DoesNotExist:
            messages.error(request, 'Profil employé non trouvé.')
            return redirect('home')
    
    return render(request, 'tasks/task_detail.html', {'task': task})

@login_required
def task_create(request):
    if request.user.user_type not in ['admin', 'project_manager']:
        messages.error(request, 'Accès non autorisé.')
        return redirect('home')
    
    if request.method == 'POST':
        form = TacheForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            # Set the user who created the task
            try:
                employee = Employee.objects.get(user=request.user)
                task.attribuee_par = employee
            except Employee.DoesNotExist:
                messages.error(request, 'Profil employé non trouvé.')
                return redirect('home')
            
            task.save()
            messages.success(request, 'Tâche créée avec succès.')
            return redirect('task_list')
    else:
        form = TacheForm()
    
    return render(request, 'tasks/task_form.html', {'form': form, 'title': 'Créer une tâche'})

@login_required
def task_edit(request, task_id):
    task = get_object_or_404(Tache, id=task_id)
    
    # Check permissions
    if request.user.user_type not in ['admin', 'project_manager']:
        messages.error(request, 'Accès non autorisé.')
        return redirect('home')
    
    if request.method == 'POST':
        form = TacheForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tâche modifiée avec succès.')
            return redirect('task_detail', task_id=task.id)
    else:
        form = TacheForm(instance=task)
    
    return render(request, 'tasks/task_form.html', {'form': form, 'title': 'Modifier la tâche'})

@login_required
def task_update_status(request, task_id):
    task = get_object_or_404(Tache, id=task_id)
    
    # Check permissions - employees can update their own tasks, managers can update any
    if request.user.user_type == 'employee':
        try:
            employee = Employee.objects.get(user=request.user)
            if task.employee != employee:
                messages.error(request, 'Accès non autorisé.')
                return redirect('task_list')
        except Employee.DoesNotExist:
            messages.error(request, 'Profil employé non trouvé.')
            return redirect('home')
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(Tache.STATUT_CHOICES):
            task.statut = new_status
            if new_status == 'terminee':
                task.date_completion = timezone.now().date()
            task.save()
            messages.success(request, 'Statut de la tâche mis à jour.')
        else:
            messages.error(request, 'Statut invalide.')
    
    return redirect('task_detail', task_id=task.id)

@login_required
def task_evaluate(request, task_id):
    task = get_object_or_404(Tache, id=task_id)
    
    # Only admins and project managers can evaluate tasks
    if request.user.user_type not in ['admin', 'project_manager']:
        messages.error(request, 'Accès non autorisé.')
        return redirect('home')
    
    if request.method == 'POST':
        form = TacheEvaluationForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Évaluation enregistrée avec succès.')
            return redirect('task_detail', task_id=task.id)
    else:
        form = TacheEvaluationForm(instance=task)
    
    return render(request, 'tasks/task_evaluate.html', {'form': form, 'task': task})

@login_required
def my_tasks(request):
    """View for employees to see only their assigned tasks"""
    try:
        employee = Employee.objects.get(user=request.user)
        tasks = Tache.objects.filter(employee=employee).order_by('-date_creation')
        
        # Filter by status if provided
        status_filter = request.GET.get('status')
        if status_filter:
            tasks = tasks.filter(statut=status_filter)
        
        paginator = Paginator(tasks, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        return render(request, 'tasks/my_tasks.html', {
            'page_obj': page_obj,
            'status_filter': status_filter,
            'status_choices': Tache.STATUT_CHOICES
        })
    except Employee.DoesNotExist:
        messages.error(request, 'Profil employé non trouvé.')
        return redirect('home')