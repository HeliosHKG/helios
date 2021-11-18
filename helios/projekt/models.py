from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.enums import Choices
from django.db.models.fields import CharField, IntegerField, TextField, FloatField
from django.db.models.fields.related import ForeignKey, ManyToManyField

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
    gewerk2 = CharField(max_length=50)

    def __str__(self):
        return self.gewerk2


class Klassifizierung(models.Model):
    klassifizierung = CharField(max_length=50)

    def __str__(self):
        return self.klassifizierung


class Input_Klassifizierung(models.Model):
    klassifizierung = ForeignKey(Klassifizierung, on_delete=SET_NULL, null=True)
    gewerk2 = ForeignKey(Gewerk2, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.pk


class Energietraeger(models.Model):
    energietraeger = CharField(max_length=50)
    gewerk = ForeignKey(Gewerk, on_delete=SET_NULL, null=True)
    treibhausgasemission=FloatField()
    nationaler_gew_faktor=FloatField()

    def __str__(self):
        return self.energietraeger


class Input_Energietraeger(models.Model):
    energietraeger = ForeignKey(Energietraeger, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.pk
  

class Umwandlung(models.Model):
    umwandlung = CharField(max_length=50)
    gewerk = ForeignKey(Gewerk, on_delete=SET_NULL, null=True)
    gewerk2 = ForeignKey(Gewerk2, on_delete=SET_NULL, null=True)
    wirkungsgrad = FloatField()
    energietraeger = ManyToManyField(Energietraeger, null=True)

    def __str__(self):
        return self.umwandlung

class Input_Umwandlung(models.Model):
    umwandlung_Pro_Gewerk=ForeignKey(Umwandlung,on_delete=SET_NULL,null=True)

    def __str__(self):
        return self.pk
    

class Abgabesystem_HLKS(models.Model):
    abgabesystem = CharField(max_length=50)
    gewerk = ForeignKey(Gewerk, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.abgabesystem


class Input_Abgabesystem(models.Model):
    abgabesystem = ForeignKey(Abgabesystem_HLKS, on_delete=SET_NULL, null=True)
    gebaudenutzung = ForeignKey(Gebaudenutzung, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.pk


class Erzeugungstyp(models.Model):
    erzeugungstyp = CharField(max_length=50)

    def __str__(self):
        return self.erzeugungstyp


class Input_Unterhaltsfaktor(models.Model):
    unterhaltsfaktor_Pro_Gewerk=FloatField()
    gewerk=ForeignKey(Gewerk,on_delete=SET_NULL,null=True)

    def __str__(self):
        return self.unterhaltsfaktor_Pro_Gewerk

class Input_Energiepreise(models.Model):
    energiepreis_Pro_Energietraeger=FloatField()
    energietraeger=ForeignKey(Energietraeger,on_delete=SET_NULL,null=True)

    def __str__(self):
        return self.energiepreis_Pro_Energietraeger    
    
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
        return self.projekt_name or ''


class ProjektSpezifikationen(models.Model):

    projekt_name = ForeignKey(Projekt, on_delete=CASCADE, null=True, blank=True)
    projekt_raumnutzung = ForeignKey(Raumnutzung, on_delete=SET_NULL, null=True)
    projekt_gewerk = ManyToManyField(Gewerk, null=True)
    projekt_raumflaeche = IntegerField(null=True, blank=True)

    projekt_raumhoehe = FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.projekt_raumflaeche)


class Kostenstammdaten_Elektro(models.Model):

    einheitspreis_pro_m2 = FloatField(null=True, blank=True)
    gebaudenutzung = ForeignKey(Gebaudenutzung, on_delete=CASCADE, null=True, blank=True)
    raumnutzung = ForeignKey(Raumnutzung, on_delete=CASCADE, null=True, blank=True)
    gewerk = ForeignKey(Gewerk, on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.einheitspreis_pro_m2)


class Kostenstammdaten_HLKS_Abgabe(models.Model):
    einheitspreis_pro_m2 = FloatField(null=True, blank=True)
    gebaudenutzung = ForeignKey(Gebaudenutzung, on_delete=CASCADE, null=True, blank=True)
    raumnutzung = ForeignKey(Raumnutzung, on_delete=CASCADE, null=True, blank=True)
    gewerk = ForeignKey(Gewerk, on_delete=CASCADE, null=True, blank=True)
    abgabesystem = ForeignKey(Abgabesystem_HLKS, on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.einheitspreis_pro_m2) or ''


class Kostenstammdaten_HLKS_Erzeugung(models.Model):
    einheitspreis_pro_KW = FloatField(blank=True, null=True)
    umwandlung = ForeignKey(Umwandlung, on_delete=SET_NULL, blank=True, null=True)
    gewerk = ForeignKey(Gewerk, on_delete=CASCADE, blank=True, null=True)
    einheitspreis_pro_m3 = FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.einheitspreis_pro_KW) or ''


class Nutzungsstammdaten_SIA2024(Model):
    raumnutzung = ForeignKey(Raumnutzung, on_delete=SET_NULL, null=True)
    klassefizierung = models.ForeignKey(Klassifizierung, on_delete=SET_NULL, null=True)
    gewerk2 = ForeignKey(Gewerk2, on_delete=SET_NULL, null=True)
    leistung_pro_m2_Klassefizierung_Gewerk2 = FloatField(null=True, blank=True)
    energie_pro_m2_Klassefizierung_Gewerk2 = FloatField(null=True, blank=True)
    raumtemparatur_sommer = FloatField(null=True, blank=True)
    raumtemparatur_winter = FloatField(null=True, blank=True)
    luftwechsel_Pro_Person = FloatField(null=True, blank=True)
    flaeche_Pro_Personenanzahl = FloatField(null=True, blank=True)
    beleuchtungsstaerke = FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.raumtemparatur_sommer)


class Stammdaten_Technickzentralen_Elektro(models.Model):
    leistung_pro_m2_von = FloatField(blank=True, null=True)
    leistung_pro_m2_bis = FloatField(blank=True, null=True)
    gebaudegroesse_von = FloatField(blank=True, null=True)
    gebaudegroesse_bis = FloatField(blank=True, null=True)
    zentraltyp = CharField(max_length=50)
    zentralengroesse = FloatField(blank=True, null=True)


    def __str__(self):
        return self.zentraltyp


class Technikzentralstammdaten_HLKS(models.Model):
    leistung_Pro_Gewerk_Therm_von = FloatField(blank=True, null=True)
    leistung_Pro_Gewerk_Therm_bis = FloatField(blank=True, null=True)
    luftmenge_von = FloatField(blank=True,null=True)
    luftmenge_bis = FloatField(blank=True,null=True)
    gewerk = ForeignKey(Gewerk, on_delete=SET_NULL, blank=True,null=True)
    umwandlung=ForeignKey(Umwandlung,on_delete=SET_NULL,blank=True,null=True)
    erzeugungstyp = ForeignKey(Erzeugungstyp, on_delete=SET_NULL, blank=True,null=True)
    zentralentyp = CharField(max_length=50, blank=True,null=True)
    zentralengroesse = FloatField(blank=True, null=True)

    def __str__(self):
        return self.pk or ''

    
    
class Csv(models.Model):
    file_name = models.FileField(upload_to='csvs')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False) 
    
    def __str__(self):
        return f"File id: {self.id}"    

