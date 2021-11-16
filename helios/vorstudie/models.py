from typing import Generic
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from .models import Projekt


class Raumnutzung(models.Model):
    raumnutzung = models.CharField(max_length=50)
    
    def __init__(self):
        return self.raumnutzung




