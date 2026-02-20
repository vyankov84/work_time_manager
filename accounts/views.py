from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from .models import Employee
from .forms import EmployeeForm


def employee_list(request: HttpRequest) -> HttpResponse:

    employees = Employee.objects.all().order_by('first_name')

    return render(request, 'accounts/employee-list.html', {'employees': employees})


def employee_details(request: HttpRequest, pk: int) -> HttpResponse:

    employee = get_object_or_404(Employee, pk=pk)

    return render(request, 'accounts/employee-details.html', {'employee': employee})


def employee_create(request: HttpRequest) -> HttpResponse:

    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('accounts:employee-list')
    else:
        form = EmployeeForm()

    context = {'form': form, 'title': 'Add New Employee'}

    return render(request, 'accounts/employee-form.html', context)


def employee_update(request: HttpRequest, pk: int) -> HttpResponse:
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':

        form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()
            return redirect('accounts:employee-details', pk=employee.pk)
    else:
        form = EmployeeForm(instance=employee)

    context = {
        'form': form,
        'title': 'Edit Employee'
    }

    return render(request, 'accounts/employee-form.html', context)
