from django import forms
from django.core.exceptions import ValidationError
from .models import Project, validate_job_number_region


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project

        fields = [
            'job_number', 'name', 'client_name', 'region', 'project_status',
            'expected_work_hours', 'assigned_employees'
        ]

        widgets = {
            'job_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Example: 111-XXXX',
                }
            ),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter project title'
            }),
            'client_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Client company name'
            }),
            'region': forms.Select(attrs={'class': 'form-select'}),
            'project_status': forms.Select(attrs={'class': 'form-select'}),
            'expected_work_hours': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0'
            }),
            'assigned_employees': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                    'style': 'height: 150px;',
                    'help_text': 'Hold Ctrl (or Cmd) to select multiple'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields['job_number'].widget.attrs['readonly'] = True
            self.fields['job_number'].help_text = "Job number cannot be edited"
        else:
            self.fields['job_number'].help_text = (
                "Prefixes: 111 (EMEA), 222 (APAC), 333 (NA), 444 (LATAM)"
            )

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name and len(name) < 5:
            raise ValidationError("Project name must be at least 5 characters long.")
        return name


    def clean(self):
        cleaned_data = super().clean()
        job_number = cleaned_data.get("job_number")
        region = cleaned_data.get("region")

        if self.instance and self.instance.pk:
            job_number = self.instance.job_number

        if job_number and region:
            try:
                validate_job_number_region(job_number, region)
            except ValidationError as e:
                self.add_error("job_number", e.message)

        return cleaned_data