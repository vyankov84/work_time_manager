from django.db import models

from accounts.models import Employee
from projects.models import Project


class Activity(models.Model):

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='activities'
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='activities'
    )

    task_name = models.CharField(
        max_length=150,
    )

    date = models.DateField(
        help_text="The day the work was performed",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    hours_worked = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        help_text="Total time spent on the task",
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name_plural = "Activities"
        ordering = ['-date', '-created_at']

    def __str__(self):
        return f"{self.task_name} - {self.employee.last_name} ({self.date})"

