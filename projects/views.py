from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum, Value, FloatField
from django.db.models.functions import Coalesce
from django.http import HttpRequest, HttpResponse

from accounts.models import Employee
from activities.models import Activity
from .forms import ProjectForm
from .models import Project



def dashboard(request: HttpRequest) -> HttpResponse:

    total_projects = Project.objects.count()
    total_employees = Employee.objects.count()
    recent_activities = Activity.objects.select_related('employee', 'project').order_by('-date')[:5]

    projects_with_hours = Project.objects.annotate(
        total_hours=Coalesce(
            Sum('activities__hours_worked'),
            Value(0.0),
            output_field=FloatField()
        )).order_by('-total_hours')[:8]

    context = {
        'total_projects': total_projects,
        'total_employees': total_employees,
        'recent_activities': recent_activities,
        'projects_with_hours': projects_with_hours,
        'page_title': 'Dashboard'
    }
    return render(request, 'projects/dashboard.html', context)


def project_list(request: HttpRequest) -> HttpResponse:

    projects = Project.objects.all().order_by('-id')

    context = {'projects': projects}

    return render(request, 'projects/project-list.html', context)


def project_details(request: HttpRequest, pk: int) -> HttpResponse:

    project = get_object_or_404(Project, pk=pk)

    context = {'project': project}

    return render(request, 'projects/project-details.html', context)


def project_create(request: HttpRequest) -> HttpResponse:

    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('projects:project-list')
    else:
        form = ProjectForm()

    context = {
        'form': form,
        'title': 'Create Project'
    }

    return render(request, 'projects/project-form.html', context)


def project_update(request: HttpRequest, pk: int) -> HttpResponse:

    project = get_object_or_404(Project, pk=pk)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects:project-detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)

    context = {
        'form': form,
        'title': 'Update Project'
    }

    return render(request, 'projects/project-form.html', context)


def project_delete(request: HttpRequest, pk: int) -> HttpResponse:

    project = get_object_or_404(Project, pk=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('projects:project-list')

    context = {'project': project}

    return render(request, 'projects/project-confirm-delete.html', context)

