from rest_framework import serializers
from farm.models import Animal, Species, FoodStock, Tasks, HealthLog, ProductionLog, WeatherLog
from core.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'created_at']

class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ['id', 'name', 'production_type']

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['id','user','species','tag_number','name','breed','weight',
                    'health_status','hatched_or_born','created_at']

class FoodStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodStock
        fields = ['id','user','item_name','quantity','unit',
                  'expiry_date','daily_consumption_estimate','created_at']
        

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model =Tasks
        fields = ['id','user','title','description','task_type',
                  'due_date','completed','created_at']
        read_only_fields = ['created_at'] # Making created_at read-only

class healthLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthLog
        fields = ['id','condition','notes','treatement',
                  'logged_at','recorded_by','animal']
        
class ProductionLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionLog
        fields = ['id','eggs_count','weight_produced',
                  'date','animal']
        
class WeatherLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherLog
        fields = ['id','temperature','humidity',
                  'condition','uv_index','user','logged_at']
        read_only_fields = ['logged_at'] # Making logged_at read-only


        
