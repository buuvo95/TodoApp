from django.db import models
from django.db.models.fields import BooleanField, CharField

class Category(models.Model):
    category = models.CharField(max_length=20, default=None)
    description = models.CharField(max_length=100, default=None)
    date_begin = models.DateField()
    check = models.BooleanField(default=False)


    def __str__(self):
        return self.category
    
    class Meta:
        ordering = ['date_begin']

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=100, default=None)
    description = models.CharField(max_length=300, default=None)
    date_begin = models.DateField()
    date_end = models.DateField()
    check = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name