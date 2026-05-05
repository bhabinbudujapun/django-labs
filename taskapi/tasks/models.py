from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200, validators=[MinLengthValidator(6)])
    description = models.TextField(blank=False, validators=[MinLengthValidator(6)])
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title