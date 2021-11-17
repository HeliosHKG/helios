from django.contrib import admin



from .models import Input_Investitionskosten, Technikflaechen, Leistung

admin.site.register(Technikflaechen)
admin.site.register(Leistung)
admin.site.register(Input_Investitionskosten)
