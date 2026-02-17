from django.contrib import admin

from activities.models import Activity


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):

    list_display = [
        'task_name',
        'employee',
        'project',
        'hours_worked',
        'date',
        'created_at',
    ]

    list_filter = [
        'date',
        'employee',
        'project'
    ]

    search_fields = [
        'task_name',
        'employee__last_name',
        'project__name'
    ]

    readonly_fields = ['created_at', 'updated_at']