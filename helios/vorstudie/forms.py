from django import forms
from .models import Investitionskosten, Leistung


class LeistungModelForm(forms.ModelForm):
    
    class Meta:
        model = Leistung 
        fields = (
            "projekt",
            "klassifizierung",
            "gewerk2",
            "leistung_pro_m2_Klassifizierung_Gewerk2",
            "luftwechsel_pro_Person_Klassifizierung",
            "flaeche_pro_Personenanzahl_Klassifizierung",
            
            "leistung_pro_gewerk",
            "personenanzahl_pro_nutzung",
            "luftwechsel_pro_nutzung",
            
           
                    
            )  
        
class InvestitionskostenModelForm(forms.ModelForm):
    
    class Meta:
        model = Investitionskosten 
        fields = (
            "projekt",
            "flaeche",
            "leistung",
            "gewerk",
            "umwandlung",
            "stammdaten_kosten_hlks_abgabe",
            "stammdaten_kosten_hlks_erzeugung",
            "stammdateb_kosten_elektro",
            
            "investitionskosten_m2_gewerk",
            "investitionskosten_Kw_Gewerk_Erzeugung",
            "investitionskosten_Kw_Gewerk_Erzeugung2",
            
           
                    
            )  