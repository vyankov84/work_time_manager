from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import ForeignKey

from accounts.models import Employee
from projects.choices import RegionType, ProjectStatus
from projects.validators import validate_job_number_region


class Project(models.Model):

    name = models.CharField(
        max_length=200,
    )

    job_number = models.CharField(
        max_length=10,
        unique=True,
        help_text='Format: 111XXXXXXX for EMEA, 222XXXXXXX for APAC, etc.',
    )

    client_name = models.CharField(
        max_length=200,
    )

    region = models.CharField(
        max_length=10,
        choices=RegionType.choices,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    expected_work_hours = models.IntegerField(
        validators=[
            MinValueValidator(0),
        ],
        default=0,
    )

    project_status = models.CharField(
        max_length=10,
        choices=ProjectStatus.choices,
        default=ProjectStatus.PENDING,
    )

    project_manager = ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='managed_projects',
    )

    assigned_employees = models.ManyToManyField(
        Employee,
        related_name='projects',
        blank=True,
    )

    def clean(self):
        super().clean()
        validate_job_number_region(self.job_number, self.region)

    def __str__(self):
        return f"{self.name} - {self.job_number}"
