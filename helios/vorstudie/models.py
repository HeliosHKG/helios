from typing import Callable, Generic
from django.db.models import Model
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.fields import CharField, FloatField, IntegerField
from django.db.models.fields.related import ForeignKey


class Input_Investitionskosten(Model):
    projekt = ForeignKey("projekt.Projekt", on_delete=CASCADE, null=True, blank=True)
    flaeche = IntegerField()
    gebaudenutzung = ForeignKey("projekt.Gebaudenutzung", on_delete=SET_NULL, null=True)
    raumnutzung = ForeignKey("projekt.Raumnutzung", on_delete=SET_NULL, null=True)
    gewerk = ForeignKey("projekt.Gewerk", on_delete=SET_NULL, null=True)
    abgabesystem = ForeignKey("projekt.Abgabesystem", on_delete=SET_NULL, null=True)
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



