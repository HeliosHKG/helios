from typing import Callable, Generic
from django.db import models
from django.db.models.deletion import CASCADE, SET, SET_NULL
from django.db.models.fields import CharField, FloatField, IntegerField
from django.db.models.fields.related import ForeignKey

from helios.projekt.models import Abgabesystem, Erzeugungstyp, Gebaudenutzung, Gewerk, Gewerk2, Klassifizierung, Kostenstammdaten_Elektro, Kostenstammdaten_HLKS_Abgabe, Nutzungsstammdaten_SIA2024, Projekt, ProjektSpezifikationen, Raumnutzung


class Input_Investitionskosten(models.Model):
    projekt = ForeignKey(Projekt, on_delete=CASCADE, null=True, blank=True)
    flaeche = IntegerField()
    gebaudenutzung = ForeignKey(Gebaudenutzung, on_delete=SET_NULL, null=True)
    raumnutzung = ForeignKey(Raumnutzung, on_delete=SET_NULL, null=True)
    gewerk = ForeignKey(Gewerk, on_delete=SET_NULL, null=True)
    abgabesystem = ForeignKey(Abgabesystem, on_delete=SET_NULL, null=True)
    einheitspreis_pro_m2_elektro = IntegerField()
    einheitspreis_pro_m2_hlks_abgabe = IntegerField()
    einheitspreis_pro_m2_hlks_erzeugung = IntegerField()

    def __str__(self):
        return self.projekt or ''

    def __str__(self):
        return self

    def __init__(self):
        self.einheitspreis_pro_m2_hlks_abgabe = self.getSanitaerKostenAbgabe + \
            self.getHeizungsKostenAbgabe + self.getLueftungsKostenAbgabe + self.getKaeltKostenAbgabe
        return self

    def getElektroKostenAbgabe(self):
        kostenstammdaten_Elektro: Kostenstammdaten_Elektro = Kostenstammdaten_Elektro.objects.get(
            gewerk=self.gewerk, raumnutzung=self.raumnutzung, gebaudenutzung=self.gebaudenutzung)
        pro_m2 = kostenstammdaten_Elektro.einheitspreis_pro_m2
        return pro_m2 * self.flaeche

    def getSanitaerKostenAbgabe(self):
        kostenstammdaten_HLKS_Abgabe: Kostenstammdaten_HLKS_Abgabe = Kostenstammdaten_HLKS_Abgabe.objects.get(
            gewerk=self.gewerk, raumnutzung=self.raumnutzung, abgabesystem=self.abgabesystem, gebaudenutzung=self.gebaudenutzung)
        pro_m2 = kostenstammdaten_HLKS_Abgabe.einheitspreis_pro_m2
        return pro_m2 * self.flaeche

    def getHeizungsKostenAbgabe(self):
        kostenstammdaten_HLKS_Abgabe: Kostenstammdaten_HLKS_Abgabe = Kostenstammdaten_HLKS_Abgabe.objects.get(
            gewerk=self.gewerk, raumnutzung=self.raumnutzung, abgabesystem=self.abgabesystem, gebaudenutzung=self.gebaudenutzung)
        pro_kw = kostenstammdaten_HLKS_Abgabe.einheitspreis_pro_m2
        return pro_kw

    def getLueftungsKostenAbgabe(self):
        kostenstammdaten_HLKS_Abgabe: Kostenstammdaten_HLKS_Abgabe = Kostenstammdaten_HLKS_Abgabe.objects.get(
            gewerk=self.gewerk, raumnutzung=self.raumnutzung, abgabesystem=self.abgabesystem, gebaudenutzung=self.gebaudenutzung)
        pro_m3h = kostenstammdaten_HLKS_Abgabe.einheitspreis_pro_m2
        return pro_m3h

    def getKaeltKostenAbgabe(self):
        kostenstammdaten_HLKS_Abgabe: Kostenstammdaten_HLKS_Abgabe = Kostenstammdaten_HLKS_Abgabe.objects.get(
            gewerk=self.gewerk, raumnutzung=self.raumnutzung, abgabesystem=self.abgabesystem, gebaudenutzung=self.gebaudenutzung)
        pro_kw = kostenstammdaten_HLKS_Abgabe.einheitspreis_pro_m2
        return pro_kw


class Technikflaechen(models.Model):
    projekt = ForeignKey(Projekt, on_delete=SET_NULL, null=True)
    stammdaten_technikzentrale_elektro = FloatField()
    stammdaten_technikzentrale_hlks = FloatField()
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

    def __str__(self):
        return str(self.leistung_pro_m2_Klassifizierung_Gewerk2)


