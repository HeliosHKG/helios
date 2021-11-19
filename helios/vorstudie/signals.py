from django.db.models.expressions import Exists
from django.db.models import signals
from django.db.models.fields import IntegerField
from django.db.models.signals import post_save, post_init
from django.dispatch import receiver

from helios.projekt.models import (
    Abgabesystem_HLKS,
    Gebaudenutzung,
    Gewerk2,
    Kostenstammdaten_Elektro,
    Kostenstammdaten_HLKS_Abgabe, 
    Nutzungsstammdaten_SIA2024,
    Projekt, 
    ProjektSpezifikationen, 
    Stammdaten_Technickzentralen_Elektro,
    Gewerk,
    Kostenstammdaten_HLKS_Erzeugung
    
)

from .models import (
    Investitionskosten,
    Leistung,
    Technikflaechen,
)

@receiver(post_save, sender=Leistung)
def create_leistung(sender, instance, **kwargs):
    
    projekt_pk = instance.projekt_id
    
    raumnutzung:ProjektSpezifikationen = ProjektSpezifikationen.objects.get(projekt_name = projekt_pk)
    flaeche = raumnutzung.projekt_raumflaeche
    nutzung = raumnutzung.projekt_raumnutzung
    
    data_stamm_2024:Nutzungsstammdaten_SIA2024 = Nutzungsstammdaten_SIA2024.objects.get(raumnutzung = nutzung, gewerk2 = instance.gewerk2, klassefizierung = instance.klassifizierung)
    
    Leistung.objects.filter(projekt_id = projekt_pk).update(leistung_pro_m2_Klassifizierung_Gewerk2=data_stamm_2024.leistung_pro_m2_Klassefizierung_Gewerk2)
    Leistung.objects.filter(projekt_id = projekt_pk).update(luftwechsel_pro_Person_Klassifizierung = data_stamm_2024.luftwechsel_Pro_Person)
    Leistung.objects.filter(projekt_id = projekt_pk).update(flaeche_pro_Personenanzahl_Klassifizierung = data_stamm_2024.flaeche_Pro_Personenanzahl)
    
    leistung_pro_m2 = data_stamm_2024.leistung_pro_m2_Klassefizierung_Gewerk2
    person_pro_m2 = data_stamm_2024.flaeche_Pro_Personenanzahl
    luftwechsel_pro_person = data_stamm_2024.luftwechsel_Pro_Person
    
    #Berechnung Leistung pro Gewerk
    res_Leistung_pro_Gewerk = (flaeche * leistung_pro_m2)
    res_Personanzahl_pro_nutzung = (flaeche / person_pro_m2)
    res_luftwechsel_pro_nutzung = (res_Personanzahl_pro_nutzung*luftwechsel_pro_person)
    
    #Berechnungen Update
    
    Leistung.objects.filter(projekt_id = projekt_pk).update(leistung_pro_gewerk=res_Leistung_pro_Gewerk)
    Leistung.objects.filter(projekt_id = projekt_pk).update(personenanzahl_pro_nutzung=res_Personanzahl_pro_nutzung)
    Leistung.objects.filter(projekt_id = projekt_pk).update(luftwechsel_pro_nutzung=res_luftwechsel_pro_nutzung)
    
@receiver(post_save, sender=Investitionskosten)
def create_investitionskosten(sender, instance, **kwargs):
    
    projekt_pk = instance.projekt_id
    
    raumnutzung:ProjektSpezifikationen = ProjektSpezifikationen.objects.get(projekt_name = projekt_pk)
    flaeche = raumnutzung.projekt_raumflaeche
    nutzung = raumnutzung.projekt_raumnutzung
    nutzung_geb = raumnutzung.projekt_gebauedenutzung
    
    
    
    Investitionskosten.objects.filter(projekt_id = projekt_pk).update(flaeche=flaeche)
    einheit_pro_m2 = 0
    einheit_pro_m3 = 0
    try:
        data_stamm_hlks_abgabe:Kostenstammdaten_HLKS_Abgabe = Kostenstammdaten_HLKS_Abgabe.objects.get(raumnutzung = nutzung, gewerk = instance.gewerk, gebaudenutzung = nutzung_geb, abgabesystem = instance.abgabesystem) #TODO eigentlich müsste dies Gebäudenutzung sein
        Investitionskosten.objects.filter(projekt_id = projekt_pk).update(stammdaten_kosten_hlks_abgabe=data_stamm_hlks_abgabe.einheitspreis_pro_m2)
    except:
        pass
    
    abgabesystem_e:Kostenstammdaten_HLKS_Erzeugung = Kostenstammdaten_HLKS_Erzeugung.objects.get(gewerk = instance.gewerk, umwandlung = instance.umwandlung)
    if abgabesystem_e.einheitspreis_pro_KW != 0:
        
        einheit_pro_m2 = Investitionskosten.objects.filter(projekt_id = projekt_pk).update(stammdaten_kosten_hlks_erzeugung= abgabesystem_e.einheitspreis_pro_KW)
    else:
        
        einheit_pro_m3 = Investitionskosten.objects.filter(projekt_id = projekt_pk).update(stammdaten_kosten_hlks_erzeugung = abgabesystem_e.einheitspreis_pro_m3)
    
    try:
        elektro_kosten:Kostenstammdaten_Elektro = Kostenstammdaten_Elektro.objects.get(raumnutzung = nutzung, gewerk = instance.gewerk, gebaudenutzung = nutzung_geb)
        Investitionskosten.objects.filter(projekt_id = projekt_pk).update(stammdaten_kosten_elektro=elektro_kosten.einheitspreis_pro_m2)
    except:
        pass
    
    # Investitionskosten pro m2 
    
    investitionskosten_m2 = flaeche * (einheit_pro_m2+einheit_pro_m3)
    Investitionskosten.objects.filter(projekt_id = projekt_pk).update(investitionskosten_m2_gewerk = investitionskosten_m2)
    
    leistung_pro_gewerk:Leistung = Leistung.objects.get(projekt_id = projekt_pk)
    lk = leistung_pro_gewerk.leistung_pro_gewerk
    
    investitionskosten_kw = lk * (einheit_pro_m2+einheit_pro_m3)
    Investitionskosten.objects.filter(projekt_id = projekt_pk).update(investitionskosten_Kw_Gewerk_Erzeugung = investitionskosten_kw)


#Berechnung Technikflaechen
@receiver(post_save, sender=Technikflaechen)
def create_investitionskosten(sender, instance, **kwargs):
    
    projekt_pk = instance.projekt_id
    
    raumnutzung:ProjektSpezifikationen = ProjektSpezifikationen.objects.get(projekt_name = projekt_pk)
    flaeche = raumnutzung.projekt_raumflaeche
    raumhoehe = raumnutzung.projekt_raumhoehe
    nutzung = raumnutzung.projekt_raumnutzung
    nutzung_geb = raumnutzung.projekt_gebauedenutzung
    
    
    # Investitionskosten.objects.filter(projekt_id = projekt_pk).update(flaeche=flaeche)
    # einheit_pro_m2 = 0
    # einheit_pro_m3 = 0
    # try:
    #     data_stamm_hlks_abgabe:Kostenstammdaten_HLKS_Abgabe = Kostenstammdaten_HLKS_Abgabe.objects.get(raumnutzung = nutzung, gewerk = instance.gewerk, gebaudenutzung = nutzung_geb, abgabesystem = instance.abgabesystem) #TODO eigentlich müsste dies Gebäudenutzung sein
    #     Investitionskosten.objects.filter(projekt_id = projekt_pk).update(stammdaten_kosten_hlks_abgabe=data_stamm_hlks_abgabe.einheitspreis_pro_m2)
    # except:
    #     pass
    
    # abgabesystem_e:Kostenstammdaten_HLKS_Erzeugung = Kostenstammdaten_HLKS_Erzeugung.objects.get(gewerk = instance.gewerk, umwandlung = instance.umwandlung)
    # if abgabesystem_e.einheitspreis_pro_KW != 0:
        
    #     einheit_pro_m2 = Investitionskosten.objects.filter(projekt_id = projekt_pk).update(stammdaten_kosten_hlks_erzeugung= abgabesystem_e.einheitspreis_pro_KW)
    # else:
        
    #     einheit_pro_m3 = Investitionskosten.objects.filter(projekt_id = projekt_pk).update(stammdaten_kosten_hlks_erzeugung = abgabesystem_e.einheitspreis_pro_m3)
    
    # try:
    #     elektro_kosten:Kostenstammdaten_Elektro = Kostenstammdaten_Elektro.objects.get(raumnutzung = nutzung, gewerk = instance.gewerk, gebaudenutzung = nutzung_geb)
    #     Investitionskosten.objects.filter(projekt_id = projekt_pk).update(stammdaten_kosten_elektro=elektro_kosten.einheitspreis_pro_m2)
    # except:
    #     pass
    
    leistung_pro:Leistung = Leistung.objects.get(projekt_id = projekt_pk)
    
    summe_luftwechsel:int = 0
    leistung_pro_gewerk:Leistung = Leistung.objects.filter(projekt_id = projekt_pk)
    for data in leistung_pro_gewerk:
        summe_luftwechsel += data.luftwechsel_pro_nutzung
    
    
    luftwechsel_pro_nutzung = leistung_pro.luftwechsel_pro_nutzung
    print (summe_luftwechsel)
    print(luftwechsel_pro_nutzung)
    
    
    
    
    # stamm_elektro: Stammdaten_Technickzentralen_Elektro = Stammdaten_Technickzentralen_Elektro.objects.get(luftmenge / leistung_pro_gewerk = lk)

    
    # # Investitionskosten pro m2 
    
    # investitionskosten_m2 = flaeche * (einheit_pro_m2+einheit_pro_m3)
    # Investitionskosten.objects.filter(projekt_id = projekt_pk).update(investitionskosten_m2_gewerk = investitionskosten_m2)
    
    # leistung_pro_gewerk:Leistung = Leistung.objects.get(projekt_id = projekt_pk)
    # lk = leistung_pro_gewerk.leistung_pro_gewerk
    
    # investitionskosten_kw = lk * (einheit_pro_m2+einheit_pro_m3)
    # Investitionskosten.objects.filter(projekt_id = projekt_pk).update(investitionskosten_Kw_Gewerk_Erzeugung = investitionskosten_kw)
