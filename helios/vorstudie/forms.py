from django import forms
from .models import KPI, Investitionskosten, Leistung, Technikflaechen, Energie


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

class TechnikflaechenModelForm(forms.ModelForm):
    
    class Meta:
        model = Technikflaechen 
        fields = (
            "projekt",
            "stammdaten_Technikzentrale_Elektro",
            "stammdaten_Technikzentrale_Hlks",
            "leistung_Pro_Gewerk",
            "luftwechsel_Pro_Nutzung",
            "gewerk",
            "umwandlung",
            "leistung_pro_m2",
            "luftmenge",
            
                    
            )  
        
class EnergieModelForm(forms.ModelForm):
    
    class Meta:
        model = Energie
        fields = (
            "projekt",
            "klassifizierung",
            "gewerk2",
            "stammdaten_sia",
            "umwandlung",
            
            
                    
            )  
        
class KPIModelForm(forms.ModelForm):
    
    class Meta:
        model = KPI
        fields = (
            
            "projekt",
            "leistung",
            "technikflaeche",
            "energie",
            "technikanteil",
                    
            )  