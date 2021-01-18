from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=45)
    pokemon_type = models.CharField(max_length=45)
    ability = models.CharField(max_length=45)