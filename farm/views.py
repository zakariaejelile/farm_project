from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from farm.models import Species, Animal, FoodStock, Tasks, HealthLog, ProductionLog, WeatherLog
from farm.serializers import (
    SpeciesSerializer, AnimalSerializer, FoodStockSerializer,
    TasksSerializer, healthLogSerializer, ProductionLogSerializer, WeatherLogSerializer
)

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


from django.shortcuts import render, get_object_or_404, redirect
from farm.models import Animal, FoodStock, Tasks
from farm.forms import AnimalForm, FoodStockForm, TaskForm
from django.contrib import messages

def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'farm/animal_list.html', {'animals': animals})

def animal_create(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Animal added")
            return redirect('animal-list')
    else:
        form = AnimalForm()
    return render(request, 'farm/animal_form.html', {'form': form})


def food_stock(request): 
    foods = FoodStock.objects.all()
    return render(request, 'farm/food_stock.html', {'foods': foods})


from django.contrib.auth.decorators import login_required
from django.db.models import Count

@login_required
def task_list(request):
    tasks = Tasks.objects.filter(user=request.user)
    return render(request, 'farm/task_list.html', {'tasks': tasks})


@login_required
def dashboard(request):
    context = {
        "animals_count": Animal.objects.filter(user=request.user).count(),
        "tasks_pending": Tasks.objects.filter(user=request.user, completed=False).count(),
        "food_items": FoodStock.objects.filter(user=request.user).count(),
    }
    return render(request, 'farm/dashboard.html', context)
