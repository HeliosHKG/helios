from typing import Callable, Generic
from django.db.models import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, FloatField, IntegerField
from django.db.models.fields.related import ForeignKey

from helios.projekt.models import Projekt
from .models import Gewerk, Kostenstammdaten_Elektro, Kostenstammdaten_HLKS_Abgabe


class Raumnutzung(Model):
    raumnutzung = CharField(max_length=50)
    
    def __str__(self):
        return self.raumnutzung

class Gebaudenutzung(Model):
    gebaudenutzung = CharField(max_length=50)

    def __str__(self):
       return self.gebaudenutzung

class Abgabesystem(Model):
    abgabesystem = CharField(max_length=50)

    def __str__(self):
        return self.abgabesystem



class Erzeugungstyp(Model):
    erzeugungstyp = CharField(max_length=50)

    def __str__(self):
        return self.erzeugungstyp



class Input_Investitionskosten(Model):
    projekt = ForeignKey(Projekt, on_delete=CASCADE)
    flaeche = IntegerField
    gebaudenutzung = ForeignKey(Gebaudenutzung, on_delete=CASCADE)
    raumnutzung = ForeignKey(Raumnutzung,on_delete=CASCADE)
    gewerk = ForeignKey(Gewerk,on_delete=CASCADE)
    abgabesystem = ForeignKey(Abgabesystem,on_delete=CASCADE)
    einheitspreis_pro_m2_elektro = IntegerField()
    einheitspreis_pro_m2_hlks_abgabe = IntegerField()
    einheitspreis_pro_m2_hlks_erzeugung = IntegerField()


    def __str__(self):
        self.einheitspreis_pro_m2_hlks_abgabe = self.getSanitaerKostenAbgabe + self.getHeizungsKostenAbgabe + self.getLueftungsKostenAbgabe + self.getKaeltKostenAbgabe
        return self

    def getElektroKostenAbgabe(self):
        kostenstammdaten_Elektro = Kostenstammdaten_Elektro.objects.get(gewerk = self.gewerk, raumnutzung = self.raumnutzung, gebaudenutzung = self.gebaudenutzung)
        pro_m2 = kostenstammdaten_Elektro
        return pro_m2 * self.flaeche

    def getSanitaerKostenAbgabe(self):
        kostenstammdaten_HLKS_Abgabe = Kostenstammdaten_HLKS_Abgabe.objects.get(gewerk = self.gewerk, raumnutzung = self.raumnutzung, abgabesystem = self.abgabesystem, gebaudenutzung = self.gebaudenutzung)
        pro_m2 = kostenstammdaten_HLKS_Abgabe
        return pro_m2 * self.flaeche

    def getHeizungsKostenAbgabe(self):
        kostenstammdaten_HLKS_Abgabe = Kostenstammdaten_HLKS_Abgabe.objects.get(gewerk = self.gewerk, raumnutzung = self.raumnutzung, abgabesystem = self.abgabesystem, gebaudenutzung = self.gebaudenutzung)
        pro_kw = kostenstammdaten_HLKS_Abgabe
        return pro_kw
    
    def getLueftungsKostenAbgabe(self):
        kostenstammdaten_HLKS_Abgabe = Kostenstammdaten_HLKS_Abgabe.objects.get(gewerk = self.gewerk, raumnutzung = self.raumnutzung, abgabesystem = self.abgabesystem, gebaudenutzung = self.gebaudenutzung)
        pro_m3h = kostenstammdaten_HLKS_Abgabe
        return pro_m3h

    def getKaeltKostenAbgabe(self):
        kostenstammdaten_HLKS_Abgabe = Kostenstammdaten_HLKS_Abgabe.objects.get(gewerk = self.gewerk, raumnutzung = self.raumnutzung, abgabesystem = self.abgabesystem, gebaudenutzung = self.gebaudenutzung)
        pro_kw = kostenstammdaten_HLKS_Abgabe
        return pro_kw



