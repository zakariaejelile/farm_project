from django.db import models
from core.models import User

class Species(models.Model):
    name = models.CharField(max_length=100)
    production_type =models.CharField(max_length=100)  # ex: dairy, meat, wool,eggs...

    def __str__(self):
        return self.name
    
class Animal(models.Model):
    tag_number =models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    breed = models.CharField(max_length=100)
    weight = models.FloatField()  # in kg
    health_status = models.CharField(max_length=100)
    hatched_or_born =models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    species = models.ForeignKey(Species, on_delete=models.PROTECT) # LINK TO SPECIES
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # LINK TO USER

    def __str__(self):
        return f"{self.tag_number} - {self.name if self.name else 'No Name'}" #DISPLAY TAG_NUMBER AND NAME IF EXISTS
    
class FoodStock(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.FloatField()  
    unit = models.CharField(max_length=50)
    expiry_date = models.DateField(null=True, blank=True)
    daily_consumption_estimate = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    user =models.ForeignKey(User,on_delete=models.CASCADE, related_name="food_stock")  # LINK TO USER

    class Meta:
        unique_together = ('item_name', 'user')  # Ensure unique item names per user
    
    def __str__(self):
        return self.item_name
    
class Tasks(models.Model):
    title =models.CharField(max_length=200)
    description = models.TextField()
    task_type = models.CharField(max_length=100)
    due_date = models.DateTimeField(default=False) # to track when the task is due
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")  # LINK TO USER

    def __str__(self):
        return self.title
    
class HealthLog(models.Model):
    condition = models.CharField(max_length=200)
    notes = models.TextField()
    treatement = models.TextField()
    logged_at =models.DateField(auto_now_add=True)
    recorded_by = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, )  # LINK TO USER
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name="health_logs")  # LINK TO ANIMAL

    def __str__(self):
        return f"HealthLog for {self.animal} - {self.condition} on {self.logged_at}"
    
class ProductionLog(models.Model):
    eggs_count = models.IntegerField(null=True, blank=True)
    weight_produced = models.FloatField(null=True, blank=True)  # in kg
    date = models.DateField()
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name="production_logs")  # LINK TO ANIMAL

    class Meta:
        unique_together = ('animal', 'date')  # Ensure one log per animal per date

    def __str__(self):
        return f"ProductionLog for {self.animal} on {self.date}"

class WeatherLog(models.Model):
    temperature = models.FloatField()  # in Celsius
    humidity = models.FloatField()     # in percentage
    condition = models.CharField(max_length=200)  # e.g., Sunny, Rainy
    uv_index = models.IntegerField()
    logged_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="weather_logs")  # LINK TO USER

    def __str__(self):
        return f"{self.logged_at} : {self.temperature}C°, {self.condition}"
    
