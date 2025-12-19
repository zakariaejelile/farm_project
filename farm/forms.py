from django import forms
from .models import Animal, FoodStock, Tasks, HealthLog, ProductionLog , WeatherLog


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


class FoodStockForm(forms.ModelForm):
    class Meta:
        model = FoodStock
        exclude = ('user', 'created_at')

        widgets = {
            'item_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Corn, Hay, Wheat'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': 'any'
            }),
            'unit': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'kg, bags, liters'
            }),
            'expiry_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'daily_consumption_estimate': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': 'any'
            }),
        }

            

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        exclude = ('user', 'created_at')
        widgets = {
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'task_type': forms.TextInput(attrs={'class': 'form-control'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class ProductionLogForm(forms.ModelForm):
    class Meta:
        model = ProductionLog
        exclude = ('recorded_by_user',)
        widgets = {
            'animal': forms.Select(attrs={'class': 'form-select'}),
            'weight_produced': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'eggs_count': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
        }


class HealthLogForm(forms.ModelForm):
    class Meta:
        model = HealthLog
        exclude = ('recorded_by',)  

        widgets = {
            'condition': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter condition (e.g., Fever, Injury)'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Additional notes...'
            }),
            'treatement': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Treatment details...'
            }),
            'logged_at': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'animal': forms.Select(attrs={'class': 'form-control'}),
        }




class WeatherLogForm(forms.ModelForm):
    class Meta:
        model = WeatherLog
        exclude = ('recorded_by_user',)
        widgets = {
            'logged_at': forms.DateInput(attrs={'type': 'date'})
        }