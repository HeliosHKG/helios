from typing import Callable, Generic
from django.db import models
from django.db.models.deletion import CASCADE, SET, SET_NULL
from django.db.models.fields import CharField, FloatField, IntegerField
from django.db.models.fields.related import ForeignKey
from helios import projekt

from helios.projekt.models import Abgabesystem_HLKS, Erzeugungstyp, Gewerk, Gewerk2, Klassifizierung, Projekt, Stammdaten_Technickzentralen_Elektro, Technikzentralstammdaten_HLKS


class Technikflaechen(models.Model):
    projekt = ForeignKey(Projekt, on_delete=SET_NULL, null=True)
    stammdaten_technikzentrale_elektro = ForeignKey(Stammdaten_Technickzentralen_Elektro, on_delete=SET_NULL,  blank=True, null=True)
    stammdaten_technikzentrale_hlks = ForeignKey(Technikzentralstammdaten_HLKS, on_delete=SET_NULL, blank=True, null=True)
    leistung_pro_gewerk = FloatField()
    luftwechsel = FloatField()
    gewerk = ForeignKey(Gewerk, on_delete=SET_NULL, null=True)
    erzeugungstyp = ForeignKey(Erzeugungstyp, on_delete=SET_NULL, null=True)
    # Berechnete Werte
    zentralentyp = CharField(max_length=50, null=True, blank=True)
    leistung_pro_m2 = FloatField(null=True, blank=True)
    luftmenge = FloatField(null=True, blank=True)
    zentralengroessen = FloatField(null=True, blank=True)

    def __str__(self):
        return self.zentralentyp or ''


class Leistung(models.Model):
    projekt = ForeignKey(Projekt, on_delete=SET_NULL, null=True)
    klassifizierung = ForeignKey(Klassifizierung, on_delete=SET_NULL, blank=True, null=True)
    gewerk2 = ForeignKey(Gewerk2, on_delete=SET_NULL, blank=True, null=True)
    leistung_pro_m2_Klassifizierung_Gewerk2 = FloatField(blank=True, null=True)
    luftwechsel_pro_Person_Klassifizierung = FloatField(blank=True, null=True)
    flaeche_pro_Personenanzahl_Klassifizierung = FloatField(blank=True, null=True)
    raumtemparatur_Klassifizierung = FloatField(blank=True, null=True)
    # Berechnete Werte
    leistung_pro_gewerk = FloatField(blank=True, null=True)
    personenanzahl_pro_nutzung = FloatField(blank=True, null=True)
    luftwechsel_pro_nutzung = FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.leistung_pro_m2_Klassifizierung_Gewerk2)


class Investitionskosten(models.Model):
    projekt = ForeignKey(Projekt, on_delete=CASCADE, null=True, blank=True)
    flaeche = IntegerField()
    leistung = ForeignKey(Leistung, on_delete=SET_NULL, null=True)
    gewerk = ForeignKey(Gewerk, on_delete=SET_NULL, null=True)
    abgabesystem = ForeignKey(Abgabesystem_HLKS, on_delete=SET_NULL, null=True)
    einheitspreis_pro_m2 = IntegerField()
    einheitspreis_pro_kw = IntegerField()
    erzeugungstyp = ForeignKey(Erzeugungstyp, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.pk or ''

class Energie(models.Model):
    projekt = ForeignKey(Projekt, on_delete=CASCADE, null=True, blank=True)
    klassifizierung = ForeignKey(Klassifizierung,on_delete=SET_NULL,null=True)
    gewerk=ForeignKey(Gewerk,on_delete=SET_NULL,null=True)

    def __str__(self):
        return self.pk
    
class Nutzungskosten(models.Model):
    projekt = ForeignKey(Projekt,on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.pk
