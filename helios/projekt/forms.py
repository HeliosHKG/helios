from django import forms
from .models import Projekt, ProjektSpezifikationen, Csv

class ProjektModelForm(forms.ModelForm):
    
    class Meta:
        model = Projekt 
        fields = (
            
            "projekt_name",
            "projekt_nummer",
            "projekt_beschreibung",
            "projekt_dienstleistung",
            "projekt_nutzung",
            "projekt_phase",
            "projekt_branche",
            "projekt_art", 
            "projekt_nutzung",
                    
            )  
        
        
class ProjektSpezModelForm(forms.ModelForm):
    
    class Meta: 
        model = ProjektSpezifikationen
        fields = (
            
            "projekt_raumnutzung",
            "projekt_raumflaeche",
            "projekt_raumhoehe",
        )
        
class CsvModelForm(forms.ModelForm):
    
    class Meta:
        model = Csv
        fields = (  
                    
                    'file_name',      
                  )
        
        def __init__(self, *args, **kwargs):
            request = kwargs.pop("request")
            projects = Projekt.objects.filter(organisation=request.user.userprofile)
            super(CsvModelForm, self).__init__(*args, **kwargs)
            self.fields["projekt_name"].queryset = projects 