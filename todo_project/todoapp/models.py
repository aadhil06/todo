from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class MyUser(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,null=True, blank=True)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username