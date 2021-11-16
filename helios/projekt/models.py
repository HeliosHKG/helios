from django.db import models
from django.db.models.fields import CharField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from helios.users.models import User



class Projekt(models.Model):
    projekt_name = CharField(max_length=50)
    projekt_nummer = IntegerField()
    projekt_beschreibung = TextField()
    projekt_ersteller = models.ForeignKey(User , on_delete=models.CASCADE, null=True, blank=True)
    projekt_added = models.DateTimeField (auto_now_add=True)
    projekt_updated = models.DateTimeField(auto_now=True)
    
    def __init__ (self):
        return self.projekt_name 
        
