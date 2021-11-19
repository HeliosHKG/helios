from django import forms
from .models import KPI, Investitionskosten, Leistung, Technikflaechen, Energie


class LeistungModelForm(forms.ModelForm):
    
    class Meta:
        model = Leistung 
        fields = (
            "projekt",
            "klassifizierung",
            "gewerk2",
            
            
                    
            )  
        
class InvestitionskostenModelForm(forms.ModelForm):
    
    class Meta:
        model = Investitionskosten 
        fields = (
            "projekt",
            "abgabesystem", 
            "gewerk",
            "umwandlung",
        
                    
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