from django import forms
from .models import Animal, FoodStock, Tasks, HealthLog


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'
        widgets = {'hatched_or_born': forms.DateInput(attrs:={'type':'date'})}

class FoodStockForm(forms.ModelForm):
    class Meta:
        model = FoodStock
        fields = '__all__'
        

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'
        widgets = {'due_date': forms.DateTimeInput(attrs={'type':'datetime-local'})}


class HealthLogForm(forms.ModelForm):
    class Meta:
        model = HealthLog
        fields = '__all__'
        widgets = {'date_recorded': forms.DateInput(attrs={'type':'date'})}