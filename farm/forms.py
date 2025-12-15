from django import forms
from .models import Animal, FoodStock, Tasks, HealthLog


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        exclude = ('user', 'created_at')
        widgets = {
            'hatched_or_born': forms.DateInput(attrs={'type': 'date'})
        }


class FoodStockForm(forms.ModelForm):
    class Meta:
        model = FoodStock
        exclude = ('user', 'created_at')


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        exclude = ('user', 'created_at')
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }


class HealthLogForm(forms.ModelForm):
    class Meta:
        model = HealthLog
        exclude = ('recorded_by_user',)
        widgets = {
            'logged_at': forms.DateInput(attrs={'type': 'date'})
        }
