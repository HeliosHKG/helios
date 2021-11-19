from os import truncate
from typing import Callable, Generic
from django.db import models
from django.db.models.deletion import CASCADE, SET, SET_NULL
from django.db.models.fields import CharField, FloatField, IntegerField
from django.db.models.fields.related import ForeignKey
from django.utils import tree
from helios import projekt

from helios.projekt.models import Energietraeger, Erzeugungstyp, Gewerk, Gewerk2, Klassifizierung, Nutzungsstammdaten_SIA2024, Projekt, Stammdaten_Technickzentralen_Elektro, Technikzentralstammdaten_HLKS, Umwandlung


class Leistung(models.Model):
    projekt = ForeignKey(Projekt, on_delete=SET_NULL, null=True)
    klassifizierung = ForeignKey(Klassifizierung, on_delete=SET_NULL, blank=True, null=True)
    gewerk2 = ForeignKey(Gewerk2, on_delete=SET_NULL, blank=True, null=True)
    leistung_pro_m2_Klassifizierung_Gewerk2 = FloatField(blank=True, null=True)
    luftwechsel_pro_Person_Klassifizierung = FloatField(blank=True, null=True)
    flaeche_pro_Personenanzahl_Klassifizierung = FloatField(blank=True, null=True)
    # Berechnete Werte
    leistung_pro_gewerk = FloatField(blank=True, null=True)
    personenanzahl_pro_nutzung = FloatField(blank=True, null=True)
    luftwechsel_pro_nutzung = FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.projekt)


class Leistung_variabl(models.Model):
    leistung = ForeignKey(Leistung, on_delete=SET_NULL, null=True)
    variabler_Luftwechsel = FloatField(null=True)
    stammdaten_sia2024 = ForeignKey(Nutzungsstammdaten_SIA2024, on_delete=SET_NULL, null=True)
    raumtemparatur_sommer = FloatField(null=True)
    raumtemparatur_winter = FloatField(null=True)
    beleuchtungsstaerke = FloatField(null=True)
    # berechnete Werte
    leistung_Pro_Gewerk2_Lueftung = FloatField(null=True)
    leistung_Pro_Gewerk2_Beleuchtung = FloatField(null=True)
    leistung_Pro_Gewerk_Heizung = FloatField(null=True)
    leistung_Pro_Gewerk_Kaelte = FloatField(null=True)
    
    def __str__(self):
        return str(self.leistung)


class Investitionskosten(models.Model):
    anzeigename = CharField(default = 'invest', max_length=50)
    projekt = ForeignKey(Projekt, on_delete=CASCADE, null=True, blank=True)
    flaeche = FloatField(null=True, blank=True)
    leistung = ForeignKey(Leistung, on_delete=SET_NULL, null=True, blank=True)
    gewerk = ForeignKey(Gewerk, on_delete=SET_NULL, null=True, blank=True)
    umwandlung = ForeignKey(Umwandlung, on_delete=SET_NULL, null=True, blank=True)
    stammdaten_kosten_hlks_abgabe = FloatField(null=True, blank=True)
    stammdaten_kosten_hlks_erzeugung = FloatField(null=True, blank=True)
    stammdateb_kosten_elektro = FloatField(null=True, blank=True)
    # berechnete Werte
    investitionskosten_m2_gewerk = FloatField(null=True, blank=True)
    investitionskosten_Kw_Gewerk_Erzeugung = FloatField(null=True, blank=True)
    investitionskosten_Kw_Gewerk_Erzeugung2 = FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.anzeigename)


class Technikflaechen(models.Model):
    projekt = ForeignKey(Projekt, on_delete=SET_NULL, null=True)
    stammdaten_Technikzentrale_Elektro = ForeignKey(Stammdaten_Technickzentralen_Elektro, on_delete=SET_NULL, null=True)
    stammdaten_Technikzentrale_Hlks = ForeignKey(Technikzentralstammdaten_HLKS, on_delete=SET_NULL, null=True)
    leistung_Pro_Gewerk = FloatField()
    luftwechsel_Pro_Nutzung = FloatField()
    gewerk = ForeignKey(Gewerk, on_delete=SET_NULL, null=True)
    umwandlung = ForeignKey(Umwandlung, on_delete=SET_NULL, null=True)
    # Berechnete Werte
    leistung_pro_m2 = FloatField(null=True, blank=True)
    luftmenge = FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.pk) 


class Energie(models.Model):
    projekt = ForeignKey(Projekt, on_delete=CASCADE, null=True, blank=True)
    klassifizierung = ForeignKey(Klassifizierung, on_delete=SET_NULL, null=True)
    gewerk2 = ForeignKey(Gewerk2, on_delete=SET_NULL, null=True)
    stammdaten_sia = ForeignKey(Nutzungsstammdaten_SIA2024, on_delete=SET_NULL, null=True, blank=True)
    umwandlung = ForeignKey(Umwandlung, on_delete=SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.projekt)


class Energie_Variabl(models.Model):
    energie = FloatField(null=True)
    variabler_Luftwechsel = FloatField(null=True)
    stammdaten_sia2024 = ForeignKey(Nutzungsstammdaten_SIA2024, on_delete=SET_NULL, null=True)
    raumtemparatur_sommer = FloatField(null=True)
    raumtemparatur_winter = FloatField(null=True)
    beleuchtungsstaerke = FloatField(null=True)
    # berechnete Werte
    energie_pro_Gewerk2_Lüftung = FloatField(null=True)
    energie_pro_Gewerk2_Beleuchtung = FloatField(null=True)
    energie_pro_Gewerk_Heizung = FloatField(null=True)
    energie_pro_Gewerk_Kälte = FloatField(null=True)
    treibhausemissionen_pro_gewerk_lueftung = FloatField(blank=True, null=True)
    treibhausemissionen_pro_gewerk_beleuchtung = FloatField(blank=True, null=True)
    treibhausemissionen_pro_gewerk_heizung = FloatField(blank=True, null=True)
    treibhausemissionen_pro_gewerk_kaelte = FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.energie)



class Nutzungskosten(models.Model):
    projekt = ForeignKey(Projekt, on_delete=SET_NULL, blank=True, null=True)
    energieerzeuger=FloatField(blank=True, null=True) #TODO Hier den Foreignkey prüfen? nach was?
    gewerk = ForeignKey(Gewerk,on_delete=SET_NULL,blank=True, null=True)
    investitionskosten=ForeignKey(Investitionskosten,on_delete=SET_NULL,blank=True, null=True)
    unterhaltsfaktor=FloatField(blank=True, null=True) #TODO sollte ein Foreignkey sein? zu wem?
    energietraeger_Pro_Energietraeger=FloatField(blank=True, null=True) #TODO sollte ein Foreignkey sein nach was?
    #berechnete Werte
    unterhaltskosten_Pro_Gewerk=FloatField(blank=True, null=True)
    energiekosten_Pro_Gewerk=FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.projekt)


class KPI(models.Model):
    projekt = ForeignKey(Projekt, on_delete=SET_NULL, blank=True, null=True)
    leistung = ForeignKey(Leistung, on_delete=SET_NULL, blank=True, null=True)
    technikflaeche = ForeignKey(Technikflaechen, on_delete=SET_NULL, blank=True, null=True)
    energie = ForeignKey(Energie, on_delete=SET_NULL, blank=True, null=True)
    #berechnete Werte
    technikanteil = FloatField(blank=True, null=True)
    
    
    def __str__(self):
        return str(self.projekt)
    
    
    