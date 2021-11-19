from django.contrib import admin

from .models import Energie, Investitionskosten, Nutzungskosten, Technikflaechen, Leistung, Leistung_variabl

admin.site.register(Technikflaechen)
admin.site.register(Leistung)
admin.site.register(Investitionskosten)
admin.site.register(Energie)
admin.site.register(Nutzungskosten)
admin.site.register(Leistung_variabl)