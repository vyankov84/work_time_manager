from django.db import models

from accounts.choices import DepartmentType


class Employee(models.Model):

    first_name = models.CharField(
        max_length=50,
    )

    last_name = models.CharField(
        max_length=50,
    )

    email = models.EmailField(
        unique=True,
    )

    job_title = models.CharField(
        max_length=50,
    )

    department = models.CharField(
        max_length=15,
        choices=DepartmentType.choices,
        default=DepartmentType.OTHER,
    )

    date_joined = models.DateField(
        auto_now_add=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'