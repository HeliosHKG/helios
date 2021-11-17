from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import CharField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey

from helios.users.models import User

#Aktuelle Auswahlfelder / Definitionen
class ProjektDienstleistung(models.Model):
    auswahl = ["Buero", "Test", "Test2"]
    projektdienstleistung = CharField(max_length=50, Choises=auswahl)
    
    def __str__(self):
        return self.projektdienstleistung
    
class ProjektPhase(models.Model):
    projektphase = CharField(max_length=50)
    
    def __str__(self):
        return self.projektphase
    
class ProjektBranche(models.Model):
    projektbranche = CharField(max_length=50)
    
    def __str__(self):
        return self.projektbranche
    
class ProjektArt(models.Model):
    projektart = CharField(max_length=50)
    
    def __str__(self):
        return self.projektart
    
class ProjektNutzung(models.Model):
    projektnutzung = CharField(max_length=50)

#Projektmodels
class Projekt(models.Model):
    projekt_name = CharField(max_length=50)
    projekt_nummer = IntegerField()
    projekt_beschreibung = TextField(null=True, blank=True)
    projekt_dienstleistung = ForeignKey(ProjektDienstleistung, on_delete=models.SET_NULL, null=True, blank=True)
    projekt_phase = ForeignKey(ProjektPhase, on_delete=models.SET_NULL, null=True, blank=True)
    projekt_branche = ForeignKey(ProjektBranche, on_delete=models.SET_NULL, null=True, blank=True)
    projekt_art = ForeignKey(ProjektArt, on_delete=models.SET_NULL, null=True, blank=True)
    projekt_nutzung = ForeignKey(ProjektNutzung, on_delete=models.SET_NULL, null=True, blank=True)
    projekt_ersteller = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    projekt_added = models.DateTimeField (auto_now_add=True)
    projekt_updated = models.DateTimeField(auto_now=True)
    
    def __str__ (self):
        return self.projekt_nummer


class ProjektSpezifikationen(models.Model):
    
    projekt_name = ForeignKey(Projekt, on_delete=models.CASCADE, null=True, blank=True )
    projekt_raumnutzung = CharField(max_length=50)
    projekt_raumflaeche = IntegerField()
    projekt_raumhoehe = IntegerField()
    
    def __str__(self):
        return self.projekt_name
    
