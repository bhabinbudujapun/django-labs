from django.db import models
from django.core.validators import MinLengthValidator

class Category(models.Model):
    name = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    
    def __str__(self):
        return self.name

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200, validators=[MinLengthValidator(6)])
    description = models.TextField(blank=False, validators=[MinLengthValidator(6)])
    category = models.ForeignKey(
        Category, 
        null=True, 
        blank=True, 
        on_delete=models.CASCADE,
        related_name='tasks'
        )
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title