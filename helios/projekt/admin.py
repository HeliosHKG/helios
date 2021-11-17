from django.contrib import admin

from .models import (
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
