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
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }



class HealthLogForm(forms.ModelForm):
    class Meta:
        model = HealthLog
        exclude = ('recorded_by_user',)
        widgets = {
            'logged_at': forms.DateInput(attrs={'type': 'date'})
        }

from django import forms
from .models import Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = [
            "tag_number",
            "name",
            "species",
            "breed",
            "hatched_or_born",
            "weight",
            "health_status",
        ]
        widgets = {
            "tag_number": forms.TextInput(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "species": forms.Select(attrs={"class": "form-select"}),
            "breed": forms.TextInput(attrs={"class": "form-control"}),
            "hatched_or_born": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "weight": forms.NumberInput(attrs={"class": "form-control"}),
            "health_status": forms.TextInput(attrs={"class": "form-control"}),
        }
