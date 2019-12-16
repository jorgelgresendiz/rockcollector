from django.db import models

# Create your models here.


class Rocks(models.Model):
    name = models.CharField()
    origin = models.CharField()
    age = models.IntegerField()
    location = models.CharField()

    def __str__(self):
        return self.name
