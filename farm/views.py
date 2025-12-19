from django.http import HttpResponse
from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from farm.models import Species, Animal, FoodStock, Tasks, HealthLog, ProductionLog, WeatherLog
#from core.models import User
from farm.serializers import (
    SpeciesSerializer, AnimalSerializer, FoodStockSerializer,
    TasksSerializer, healthLogSerializer, ProductionLogSerializer, WeatherLogSerializer
)
from django.contrib.auth import get_user_model, logout
from django.shortcuts import render, get_object_or_404, redirect
from farm.forms import AnimalForm, FoodStockForm, HealthLogForm, TaskForm, ProductionLogForm ,HealthLogForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .utils import get_weather

User = get_user_model()

class SpeciesViewSet(viewsets.ModelViewSet):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.select_related('species','user').all()
    serializer_class = AnimalSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['tag_number','name','species__name','user__id']

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.query_params.get('user')
        species = self.request.query_params.get('species')
        if user:
            queryset = queryset.filter(user_id=user)
        if species:
            queryset = queryset.filter(species_id=species)
        return queryset

class FoodStockViewSet(viewsets.ModelViewSet):
    queryset = FoodStock.objects.all()
    serializer_class = FoodStockSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # restrict to logged-in user's stock
        return FoodStock.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TasksViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = Tasks.objects.filter(user=self.request.user)
        # add simple filters
        due = self.request.query_params.get('due_date')
        completed = self.request.query_params.get('completed')
        if completed is not None:
            qs = qs.filter(completed=(completed.lower() in ['true','1']))
        if due:
            qs = qs.filter(due_date__date=due)
        return qs

    @action(detail=True, methods=['patch'])
    def complete(self, request, pk=None):
        task = self.get_object()
        task.completed = True
        task.save()
        return Response({'status':'Task completed'})

class HealthLogViewSet(viewsets.ModelViewSet):
    queryset = HealthLog.objects.all()
    serializer_class = healthLogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        animal_id = self.kwargs.get('animal_pk')
        return HealthLog.objects.filter(animal_id=animal_id)

    def perform_create(self, serializer):
        serializer.save(recorded_by_user=self.request.user)

class ProductionLogViewSet(viewsets.ModelViewSet):
    serializer_class = ProductionLogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = ProductionLog.objects.select_related('animal').all()

class WeatherLogViewSet(viewsets.ModelViewSet):
    queryset = WeatherLog.objects.all()
    serializer_class = WeatherLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return WeatherLog.objects.filter(user=self.request.user).order_by('-logged_at')
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# ANIMAL VIEWS

@login_required
def animal_list(request):
    animals = Animal.objects.filter(user=request.user)
    return render(request, 'farm/animal_list.html', {'animals': animals})


def animal_detail(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    return render(request, "farm/animal_detail.html", {
        "animal": animal
    })

@login_required
def animal_create(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            animal = form.save(commit=False)
            animal.user = request.user
            animal.save()
            messages.success(request, "Animal added")
            return redirect('animal_list')
    else:
        form = AnimalForm()
    return render(request, 'farm/animal_form.html', {'form': form})

def animal_update(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == 'POST':
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            messages.success(request, "Animal updated")
            return redirect('animal_detail', pk=animal.pk)
    else:
        form = AnimalForm(instance=animal)

    return render(request, 'farm/animal_form_update.html', {'form': form})

def animal_delete(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == "POST":
        animal.delete()
        messages.success(request, "Animal deleted")
        return redirect('animal_list')
    return render(request, 'farm/animal_confirm_delete.html', {'animal': animal})


# TASK VIEWS
@login_required
def task_list(request):
    tasks = Tasks.objects.filter(user=request.user)
    return render(request, 'farm/task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    return render(request, "farm/task_detail.html", {
        "task": task
    })

def task_create(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        task = form.save(commit=False)  # don't save to DB yet
        task.user = request.user        # assign the logged-in user
        task.save()                     # now save to DB
        return redirect('task_list')
    return render(request, "farm/task_form.html", {"form": form})

def task_update(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated")
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)

    return render(request, 'farm/task_form_update.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    if request.method == "POST":
        task.delete()
        messages.success(request, "Task deleted")
        return redirect('task_list')
    return render(request, 'farm/task_confirm_delete.html', {'task': task})

# FOOD STOCK VIEWS
@login_required
def food_stock(request): 
    food_stocks = FoodStock.objects.filter(user=request.user)
    return render(request, 'farm/food_stock.html', {
        'food_stocks': food_stocks
    })

@login_required
def food_stock_detail(request, pk):
    food = get_object_or_404(FoodStock, pk=pk, user=request.user)
    return render(request, "farm/food_stock_detail.html", {
        "food": food
    })

@login_required
def food_stock_create(request):
    form = FoodStockForm(request.POST or None)
    if form.is_valid():
        food = form.save(commit=False)
        food.user = request.user
        food.save()
        messages.success(request, "Food stock added")
        return redirect('food_stock')
    return render(request, "farm/food_stock_form.html", {"form": form})

@login_required
def food_stock_update(request, pk):
    food = get_object_or_404(FoodStock, pk=pk, user=request.user)
    form = FoodStockForm(request.POST or None, instance=food)
    if form.is_valid():
        form.save()
        messages.success(request, "Food stock updated")
        return redirect('food_stock')
    return render(request, 'farm/food_stock_form_update.html', {'form': form})

@login_required
def food_stock_delete(request, pk):
    food = get_object_or_404(FoodStock, pk=pk, user=request.user)
    if request.method == "POST":
        food.delete()
        messages.success(request, "Food stock deleted")
        return redirect('food_stock')
    return render(request, 'farm/food_stock_confirm_delete.html', {'food': food})


# PRODUCTION LOG VIEWS
@login_required
def production_list(request):
    production_logs = ProductionLog.objects.filter(animal__user=request.user)
    return render(request, 'farm/production_list.html', {'production_logs': production_logs})

@login_required
def production_detail(request, pk):
    production = get_object_or_404(ProductionLog, pk=pk)
    return render(request, "farm/production_detail.html", {
        "production": production
    })
@login_required
def production_create(request):
    form = ProductionLogForm(request.POST or None)
    if form.is_valid():
        production = form.save(commit=False)
        production.recorded_by_user = request.user
        production.save()
        messages.success(request, "Production log added")
        return redirect('production_list')
    return render(request, "farm/production_form.html", {"form": form})

@login_required
def production_update(request, pk):
    production = get_object_or_404(ProductionLog, pk=pk)
    form = ProductionLogForm(request.POST or None, instance=production)
    if form.is_valid():
        form.save()
        messages.success(request, "Production log updated")
        return redirect('production_list')
    return render(request, 'farm/production_form_update.html', {'form': form})

@login_required
def production_delete(request, pk):
    production = get_object_or_404(ProductionLog, pk=pk)
    if request.method == "POST":
        production.delete()
        messages.success(request, "Production log deleted")
        return redirect('production_list')
    return render(request, 'farm/production_confirm_delete.html', {'production': production})


# HEALTH LOG VIEWS

def health_log_list(request):
    health_logs = HealthLog.objects.filter(recorded_by=request.user)
    return render(request, 'farm/health_log_list.html', {'health_logs': health_logs})

def health_log_detail(request, pk):
    health_log = get_object_or_404(HealthLog, pk=pk)
    return render(request, "farm/health_log_detail.html", {
        "health_log": health_log
    })

def health_log_create(request):
    form = HealthLogForm(request.POST or None)
    if form.is_valid():
        health_log = form.save(commit=False)
        health_log.recorded_by = request.user
        health_log.save()
        messages.success(request, "Health log added")
        return redirect('health_log_list')
    return render(request, "farm/health_log_form.html", {"form": form})

def health_log_update(request, pk):
    health_log = get_object_or_404(HealthLog, pk=pk)
    if request.method == 'POST':
        form = HealthLogForm(request.POST, instance=health_log)
        if form.is_valid():
            form.save()
            messages.success(request, "Health log updated")
            return redirect('health_log_detail', pk=health_log.pk)
    else:
        form = HealthLogForm(instance=health_log)

    return render(request, 'farm/health_log_form_update.html', {'form': form})  

def health_log_delete(request, pk):
    health_log = get_object_or_404(HealthLog, pk=pk)
    if request.method == "POST":
        health_log.delete()
        messages.success(request, "Health log deleted")
        return redirect('health_log_list')
    return render(request, 'farm/health_log_confirm_delete.html', {'health_log': health_log})

@login_required
def weather_data(request):
    city  = "meknes"  
    api_key  = "2ff0f2995686c35cf9505db564070d02" 
    weather = get_weather(city=city, api_key=api_key)
    return render(request, "farm/weather_data.html", {"weather": weather})


def logout_view(request):
    logout(request)
    return redirect('login')    

@login_required
def dashboard(request):
    user = request.user
    # Count
    context = {
        "animals_count": Animal.objects.filter(user=user).count(),
        "tasks_pending": Tasks.objects.filter(user=user, completed=False).count(),
        "food_items": FoodStock.objects.filter(user=user).count(),
    }

    # weather data
    weather = get_weather(city="meknes", api_key="2ff0f2995686c35cf9505db564070d02")
    context["weather"] = weather

    return render(request, 'farm/dashboard.html', context)


