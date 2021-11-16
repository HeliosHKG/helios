from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

from helios.project.models import Projekt

from .models import Projekt 


class Vorstudie (models.Model):
    projekt = ForeignKey(Projekt, on_delete=CASCADE)





