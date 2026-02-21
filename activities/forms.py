from django import forms
from .models import Activity

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['employee', 'project', 'date', 'task_name', 'hours_worked']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'employee': forms.Select(attrs={'class': 'form-control'}),
            'project': forms.Select(attrs={'class': 'form-control'}),
            'task_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What did you do?'}),
            'hours_worked': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.5'}),
        }