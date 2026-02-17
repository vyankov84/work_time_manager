from django.contrib import admin

from projects.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = ['job_number', 'name', 'region', 'project_manager', 'project_status']

    list_filter = ['region', 'project_manager', 'project_status']

