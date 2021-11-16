from typing import Generic
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey


class Raumnutzung(models.Model):
    raumnutzung = CharField(max_length=50)
    
    def __str__(self):
        return self

class Gebaudenutzung(models.Model):
    gebaudenutzung = CharField(max_length=50)

    def __str__(self):
       return self

class Abgabesystem(models.Model):
    abgabesystem = CharField(max_length=50)

    def __str__(self):
        return self

class Gewerk(models.Model):
    gewerk = CharField(max_length=50)

    def __str__(self):
        return self

class Erzeugungstyp(models.Model):
    erzeugungstyp = CharField(max_length=50)

    def __str__(self):
        return self

class Kostenstammdaten_Elektro(models.Model):
    einheitspreis_pro_m2 = float
    gebaudenutzung = ForeignKey(Gebaudenutzung, on_delete=CASCADE)
    raumnutzung = ForeignKey(Raumnutzung,on_delete=CASCADE)
    gewerk = ForeignKey(Gewerk,on_delete=CASCADE)

    def __str__(self):
        return self

    def getEinheitspreis()

class Kostenstammdaten_HLKS_Abgabe(models.Model):
    einheitspreis_pro_m2 = float
    gebaudenutzung = ForeignKey(Gebaudenutzung, on_delete=CASCADE)
    raumnutzung = ForeignKey(Raumnutzung,on_delete=CASCADE)
    gewerk = ForeignKey(Gewerk,on_delete=CASCADE)
    abgabesystem = ForeignKey(Abgabesystem,on_delete=CASCADE)

    def __str__(self):
        return self

class Kostenstammdaten_HLKS_Erzeugung(models.Model):
    einheitspreis_pro_KW = float
    erzeugungstyp = ForeignKey(Erzeugungstyp, on_delete=CASCADE)
    gewerk = ForeignKey(Gewerk,on_delete=CASCADE)

    def __str__(self):
        return self


class Input_Investitionskosten(models.Model):
    flaeche = int
    gebaudenutzung = ForeignKey(Gebaudenutzung, on_delete=CASCADE)
    raumnutzung = ForeignKey(Raumnutzung,on_delete=CASCADE)
    gewerk = ForeignKey(Gewerk,on_delete=CASCADE)
    abgabesystem = ForeignKey(Abgabesystem,on_delete=CASCADE)
    einheitspreis_pro_m2_elektro = ForeignKey(Kostenstammdaten_Elektro,on_delete=CASCADE)
    einheitspreis_pro_m2_hlks_abgabe = ForeignKey(Kostenstammdaten_HLKS_Abgabe,on_delete=CASCADE)
    einheitspreis_pro_m2_hlks_erzeugung = ForeignKey(Kostenstammdaten_HLKS_Erzeugung,on_delete=CASCADE)

    def __init__(self):
        return self

