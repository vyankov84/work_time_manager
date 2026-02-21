from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ActivityForm
from .models import Activity


def activity_list(request: HttpRequest) -> HttpResponse:

    activities = Activity.objects.select_related('employee','project').order_by('-date')

    context = {
        'activities':activities,
        'page_title':'Work Log',
    }

    return render(request, 'activities/activity-list.html', context)


def activity_create(request: HttpRequest) -> HttpResponse:

    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('activities:activity-list')
    else:
        form = ActivityForm()

    context = {
        'form':form,
        'page_title':'Work Log Hours',
    }

    return render(request, 'activities/activity-form.html', context)


def activity_update(request: HttpRequest, pk: int) -> HttpResponse:

    activity = get_object_or_404(Activity, pk=pk)

    if request.method == 'POST':
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect('activities:activity-list')
    else:
        form = ActivityForm(instance=activity)

    context = {
        'form':form,
        'page_title':'Update Log Hours',
    }

    return render(request, 'activities/activity-form.html', context)


def activity_delete(request: HttpRequest, pk: int) -> HttpResponse:

    activity = get_object_or_404(Activity, pk=pk)

    if request.method == 'POST':
        activity.delete()
        return redirect('activities:activity-list')

    context = {
        'activity':activity,
    }

    return render(request, 'activites/activity-confirm-delete.html', context)
