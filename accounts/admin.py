from django.contrib import admin

from accounts.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    list_display = ('first_name','last_name','email', 'job_title', 'department', 'date_joined')

    search_fields = ['first_name','last_name','email']

    list_filter = ['department',]



