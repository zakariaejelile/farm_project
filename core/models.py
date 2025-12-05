from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True) #to track when the user was created

    def __str__(self):
        return f"{self.name} <{self.email}>"
    

