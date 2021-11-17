from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.enums import Choices
from django.db.models.fields import CharField, IntegerField, TextField, FloatField
from django.db.models.fields.related import ForeignKey

from helios.users.models import User


# Aktuelle Auswahlfelder / Definitionen
class ProjektDienstleistung(models.Model):
    # CSV Import
    projektdienstleistung = CharField(max_length=50,)

    def __str__(self):
        return self.projektdienstleistung


class ProjektPhase(models.Model):
    CHOICES_PHASE = [("Strategische Planung", "Strategische Planung"), ("Vorstudie", "Vorstudie"), ("Vorprojekt", "Vorprojekt"), ("Bauprojekt",
                                                                                                                                  "Bauprojekt"), ("Ausschreibung", "Ausschreibung"), ("Realisierung", "Realisierung"), ("Bewirtschaftung", "Bewirtschaftung")]
    projektphase = CharField(max_length=50, choices=CHOICES_PHASE, default="Vorprojekt")

    def __str__(self):
        return self.projektphase


class ProjektBranche(models.Model):
    # CSV Import
    projektbranche = CharField(max_length=50)

    def __str__(self):
        return self.projektbranche


class ProjektArt(models.Model):
    CHOICES_ART = [("Neubau", "Neubau"), ("Umbau", "Umbau"), ("Sanierung", "Sanierung"), ("Beratung", "Beratung")]
    projektart = CharField(max_length=50, choices=CHOICES_ART, default="Vorprojekt")

    def __str__(self):
        return self.projektart

# Import aus SIA Datei 2024


class ProjektNutzung(models.Model):
    # CSV Import
    projektnutzung = CharField(max_length=50)

    def __str__(self):
        return self.projektnutzung


class Raumnutzung(models.Model):
    raumnutzung = CharField(max_length=50)

    def __str__(self):
        return self.raumnutzung


class Gebaudenutzung(models.Model):
    gebaudenutzung = CharField(max_length=50)

    def __str__(self):
        return self.gebaudenutzung


class Gewerk(models.Model):
    gewerk = CharField(max_length=50)

    def __str__(self):
        return self.gewerk

class Gewerk2(models.Model):
    gewerk = CharField(max_length=50)

    def __str__(self):
        return self.gewerk

class Klassifizierung(models.Model):
    klassifizierung = CharField(max_length=50)

    def __str__(self):
        return self.klassifizierung
    

class Abgabesystem(models.Model):
    abgabesystem = CharField(max_length=50)

    def __str__(self):
        return self.abgabesystem


class Erzeugungstyp(models.Model):
    erzeugungstyp = CharField(max_length=50)

    def __str__(self):
        return self.erzeugungstyp

# Projektmodels


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
    projekt_added = models.DateTimeField(auto_now_add=True)
    projekt_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.projekt_nummer


class ProjektSpezifikationen(models.Model):

    projekt_name = ForeignKey(Projekt, on_delete=models.CASCADE, null=True, blank=True)
    projekt_raumnutzung = ForeignKey(Raumnutzung, on_delete=CASCADE)
    projekt_gewerk = ForeignKey(Gewerk, on_delete=SET_NULL, null=True)
    projekt_raumflaeche = IntegerField()
    projekt_raumhoehe = IntegerField()

    def __str__(self):
        return self.projekt_name


class Kostenstammdaten_Elektro(models.Model):

    einheitspreis_pro_m2 = FloatField()
    gebaudenutzung = ForeignKey(Gebaudenutzung, on_delete=CASCADE, null=True, blank=True)
    raumnutzung = ForeignKey(Raumnutzung, on_delete=CASCADE)
    gewerk = ForeignKey(Gewerk, on_delete=CASCADE)

    def __str__(self):
        return self.einheitspreis_pro_m2


class Kostenstammdaten_HLKS_Abgabe(models.Model):
    einheitspreis_pro_m2 = FloatField
    gebaudenutzung = ForeignKey(Gebaudenutzung, on_delete=CASCADE, null=True, blank=True)
    raumnutzung = ForeignKey(Raumnutzung, on_delete=CASCADE, null=True, blank=True)
    gewerk = ForeignKey(Gewerk, on_delete=CASCADE, null=True, blank=True)
    abgabesystem = ForeignKey(Abgabesystem, on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        return self.einheitspreis_pro_m2


class Kostenstammdaten_HLKS_Erzeugung(models.Model):
    einheitspreis_pro_KW = FloatField
    erzeugungstyp = ForeignKey(Erzeugungstyp, on_delete=CASCADE)
    gewerk = ForeignKey(Gewerk, on_delete=CASCADE)

    def __str__(self):
        return self.einheitspreis_pro_KW


class Nutzungsstammdaten_SIA2024(Model):
    raumnutzung = ForeignKey(Raumnutzung, on_delete=SET_NULL, null=True)
    klassifizierung = models.ForeignKey(Klassifizierung, on_delete=SET_NULL,null=True)
    gewerk = ForeignKey(Gewerk2, on_delete=SET_NULL, null=True)
    leistung_pro_m2_Klassifizierung_Gewerk2 = FloatField()
    energie_pro_m2_Klassifizierung_Gewerk2 = FloatField()
    raumtemparatur = FloatField()
    luftwechsel_Pro_Person = FloatField()
    flaeche_Pro_Personenanzahl = FloatField()
    beleuchtungsstaerke = FloatField()
