from typing import Callable, Generic
from django.db.models import Model
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.fields import CharField, FloatField, IntegerField
from django.db.models.fields.related import ForeignKey

from helios.projekt.models import Abgabesystem, Erzeugungstyp, Gebaudenutzung, Gewerk, Gewerk2, Klassifizierung, Nutzungsstammdaten_SIA2024, Projekt, ProjektSpezifikationen, Raumnutzung


class Input_Investitionskosten(Model):
    projekt = ForeignKey(Projekt, on_delete=CASCADE, null=True, blank=True)
    flaeche = IntegerField()
    gebaudenutzung = ForeignKey(Gebaudenutzung, on_delete=SET_NULL, null=True)
    raumnutzung = ForeignKey(Raumnutzung, on_delete=SET_NULL, null=True)
    gewerk = ForeignKey(Gewerk, on_delete=SET_NULL, null=True)
    abgabesystem = ForeignKey(Abgabesystem, on_delete=SET_NULL, null=True)
    einheitspreis_pro_m2_elektro = IntegerField()
    einheitspreis_pro_m2_hlks_abgabe = IntegerField()
    einheitspreis_pro_m2_hlks_erzeugung = IntegerField()

    # def __str__(self):
    #     self.einheitspreis_pro_m2_hlks_abgabe = self.getSanitaerKostenAbgabe + self.getHeizungsKostenAbgabe + self.getLueftungsKostenAbgabe + self.getKaeltKostenAbgabe
    #     return self

    # def getElektroKostenAbgabe(self):
    #     kostenstammdaten_Elektro = Kostenstammdaten_Elektro.objects.get(gewerk = self.gewerk, raumnutzung = self.raumnutzung, gebaudenutzung = self.gebaudenutzung)
    #     pro_m2 = kostenstammdaten_Elektro
    #     return pro_m2 * self.flaeche

    # def getSanitaerKostenAbgabe(self):
    #     kostenstammdaten_HLKS_Abgabe = Kostenstammdaten_HLKS_Abgabe.objects.get(gewerk = self.gewerk, raumnutzung = self.raumnutzung, abgabesystem = self.abgabesystem, gebaudenutzung = self.gebaudenutzung)
    #     pro_m2 = kostenstammdaten_HLKS_Abgabe
    #     return pro_m2 * self.flaeche

    # def getHeizungsKostenAbgabe(self):
    #     kostenstammdaten_HLKS_Abgabe = Kostenstammdaten_HLKS_Abgabe.objects.get(gewerk = self.gewerk, raumnutzung = self.raumnutzung, abgabesystem = self.abgabesystem, gebaudenutzung = self.gebaudenutzung)
    #     pro_kw = kostenstammdaten_HLKS_Abgabe
    #     return pro_kw

    # def getLueftungsKostenAbgabe(self):
    #     kostenstammdaten_HLKS_Abgabe = Kostenstammdaten_HLKS_Abgabe.objects.get(gewerk = self.gewerk, raumnutzung = self.raumnutzung, abgabesystem = self.abgabesystem, gebaudenutzung = self.gebaudenutzung)
    #     pro_m3h = kostenstammdaten_HLKS_Abgabe
    #     return pro_m3h

    # def getKaeltKostenAbgabe(self):
    #     kostenstammdaten_HLKS_Abgabe = Kostenstammdaten_HLKS_Abgabe.objects.get(gewerk = self.gewerk, raumnutzung = self.raumnutzung, abgabesystem = self.abgabesystem, gebaudenutzung = self.gebaudenutzung)
    #     pro_kw = kostenstammdaten_HLKS_Abgabe
    #     return pro_kw


class Technikflächen(Model):
    projekt_spez = IntegerField()
    #stammdaten_technikzentrale_elektro =
    #stammdaten_technikzentrale_hlks =
    #leistung_pro_gewerk =
    #luftwechsel =
    gewerk = ForeignKey(Gewerk, on_delete=SET_NULL, null=True)
    erzeugungstyp = ForeignKey(Erzeugungstyp, on_delete=SET_NULL, null=True)


class Leistung(Model):
    projekt_spez = ForeignKey(ProjektSpezifikationen, on_delete=SET_NULL, null=True)
    klassifizierung = ForeignKey(Klassifizierung, on_delete=SET_NULL, null=True)
    gewerk2 = ForeignKey(Gewerk2, on_delete=SET_NULL, null=True)
    leistung_pro_m2_Klassifizierung_Gewerk2 = FloatField()
    luftwechsel_pro_Person_Klassifizierung = FloatField()
    flaeche_pro_Personenanzahl_Klassifizierung = FloatField()
    raumtemparatur_Klassifizierung = FloatField()

    def __init__(self):
        Nutzungsstammdaten_SIA2024.objects.get(
            klassifizierung=self.klassifizierung, gewerk2=self.gewerk2)
        self.leistung_pro_m2_Klassifizierung_Gewerk2 = Nutzungsstammdaten_SIA2024
     #   self.luftwechsel_pro_Person_Klassifizierung = 
     #   self.raumtemparatur_Klassifizierung =
     #   self.flaeche_pro_Personenanzahl_Klassifizierung =
        return self
