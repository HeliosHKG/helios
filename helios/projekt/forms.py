from django import forms
from .models import Projekt

class ProjektModelForm(forms.ModelForm):
    
    class Meta:
        model = Projekt 
        fields = (
            
            "projekt_name",
            "projekt_nummer",
            "projekt_beschreibung",
            
                    
            )  