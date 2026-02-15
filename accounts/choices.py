from django.db import models

class DepartmentType(models.TextChoices):
    ADMIN = 'ADMIN','ADMIN'
    HR = 'HR','HR'
    SALES = 'SALES','SALES'
    MARKETING = 'MARKETING','MARKETING'
    FINANCE = 'FINANCE','FINANCE'
    IT = 'IT','IT'
    OTHER = 'OTHER','OTHER'

