from django.contrib import admin



from .models import Energie, Investitionskosten, Nutzungskosten, Technikflaechen, Leistung

admin.site.register(Technikflaechen)
admin.site.register(Leistung)
admin.site.register(Investitionskosten)
admin.site.register(Energie)
admin.site.register(Nutzungskosten)