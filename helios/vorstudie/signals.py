from django.db.models.expressions import Exists
from django.db.models import signals
from django.db.models.signals import post_save, post_init
from django.dispatch import receiver

from helios.projekt.models import (
    Gebaudenutzung,
    Gewerk2,
    Kostenstammdaten_Elektro, 
    Nutzungsstammdaten_SIA2024,
    Projekt, 
    ProjektSpezifikationen, 
    Stammdaten_Technickzentralen_Elektro,
    Gewerk
    
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
    
    data_stamm_2024:Nutzungsstammdaten_SIA2024 = Nutzungsstammdaten_SIA2024.objects.get(raumnutzung = nutzung, gewerk = instance.gewerk2, klassifizierung = instance.klassifizierung)
    
    Leistung.objects.filter(projekt_id = projekt_pk).update(leistung_pro_m2_Klassifizierung_Gewerk2=data_stamm_2024.leistung_pro_m2_Klassifizierung_Gewerk2)
    Leistung.objects.filter(projekt_id = projekt_pk).update(luftwechsel_pro_Person_Klassifizierung = data_stamm_2024.luftwechsel_Pro_Person)
    Leistung.objects.filter(projekt_id = projekt_pk).update(flaeche_pro_Personenanzahl_Klassifizierung = data_stamm_2024.flaeche_Pro_Personenanzahl)
    Leistung.objects.filter(projekt_id = projekt_pk).update(raumtemparatur_Klassifizierung = data_stamm_2024.raumtemparatur)
    
    leistung_pro_m2 = data_stamm_2024.leistung_pro_m2_Klassifizierung_Gewerk2
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
    
