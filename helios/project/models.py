from django.db import models
from django.db.models.fields import CharField, IntegerField, TextField

# Create your models here.


class Projekt (models.Model):
    projekt_name = CharField(max_length=50)
    projekt_nummer = IntegerField()
    projekt_beschreibung = TextField()
    
    
    def __init__ (self):
        return self.projekt_name 
        
