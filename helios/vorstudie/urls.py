from django.urls import path


from .views import (
    vorstudie_view,
    leistung_create_view,
    investitionskosten_create_view, 
    technikflaechen_create_view,
    energie_create_view,
    kpi_create_view,
      
)

app_name = "vorstudie"
urlpatterns = [
    path("dashboard_vorstudie/", view=vorstudie_view, name="dashboard-project"),
    path("leistung/create", view=leistung_create_view, name="leistung-create"),
    path("investitionskosten/create", view=investitionskosten_create_view, name="investitionskosten-create"),
    path("technikflaechen/create", view=technikflaechen_create_view, name="technikflaechen-create"),
    path("energie/create", view=energie_create_view, name="energie-create"),
    path("kpi/create", view=kpi_create_view, name="kpi-create"),
    
]