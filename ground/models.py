from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Ground(models.Model):
    name = models.CharField(max_length=64)
    capacity = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
