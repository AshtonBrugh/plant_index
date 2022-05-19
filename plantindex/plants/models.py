from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=100)
    genus = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)
    plant_img = models.ImageField()
    description = models.TextField()
    color = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.name

