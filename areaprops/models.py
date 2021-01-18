from django.db import models

# Create your models here.
class Area(models.Model):
    area_name = models.CharField(max_length=200,blank=False)
    
    def __str__(self):
        return self.area_name