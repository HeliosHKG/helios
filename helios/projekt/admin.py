from django.contrib import admin

from .models import (
    Abgabesystem_HLKS,
    Energietraeger,
    Erzeugungstyp,
    Gebaudenutzung,
    Gewerk,
    Klassifizierung, 
    Gewerk2,
    Nutzungsstammdaten_SIA2024,
    Projekt, 
    ProjektDienstleistung, 
    ProjektPhase, 
    ProjektBranche, 
    ProjektArt, 
    ProjektNutzung,
    ProjektSpezifikationen,
    Raumnutzung,
    Stammdaten_Technickzentralen_Elektro,
    Technikzentralstammdaten_HLKS,
    Umwandlung,
    Gebaudenutzung, 
    Kostenstammdaten_Elektro,
    Kostenstammdaten_HLKS_Abgabe, 

)

admin.site.register(ProjektPhase)
admin.site.register(Projekt)
admin.site.register(ProjektDienstleistung)
admin.site.register(ProjektBranche)
admin.site.register(ProjektArt)
admin.site.register(ProjektNutzung)
admin.site.register(Raumnutzung)
admin.site.register(Nutzungsstammdaten_SIA2024)
admin.site.register(Gebaudenutzung)
admin.site.register(Energietraeger)
admin.site.register(Umwandlung)
admin.site.register(Gewerk2)
admin.site.register(Gewerk)
admin.site.register(Erzeugungstyp)
admin.site.register(Klassifizierung)
admin.site.register(ProjektSpezifikationen)
admin.site.register(Stammdaten_Technickzentralen_Elektro)
admin.site.register(Technikzentralstammdaten_HLKS)
admin.site.register(Abgabesystem_HLKS)
admin.site.register(Kostenstammdaten_Elektro)
admin.site.register(Kostenstammdaten_HLKS_Abgabe)

