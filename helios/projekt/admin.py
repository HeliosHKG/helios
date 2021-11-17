from django.contrib import admin

from .models import (
    Erzeugungstyp,
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
    Raumnutzung,
)

admin.site.register(ProjektPhase)
admin.site.register(Projekt)
admin.site.register(ProjektDienstleistung)
admin.site.register(ProjektBranche)
admin.site.register(ProjektArt)
admin.site.register(ProjektNutzung)
admin.site.register(Raumnutzung)
admin.site.register(Nutzungsstammdaten_SIA2024)
admin.site.register(Gewerk2)
admin.site.register(Gewerk)
admin.site.register(Erzeugungstyp)
admin.site.register(Klassifizierung)