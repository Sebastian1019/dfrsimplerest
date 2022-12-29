from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    correoElectronico = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True) 
