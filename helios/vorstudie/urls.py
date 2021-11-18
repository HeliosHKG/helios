from django.urls import path


from .views import (
    vorstudie_view,
    leistung_create_view,
    investitionskosten_create_view
    
    
)

app_name = "vorstudie"
urlpatterns = [
    path("dashboard_vorstudie/", view=vorstudie_view, name="dashboard-project"),
    path("leistung/create", view=leistung_create_view, name="leistung-create"),
    path("investitionskosten/create", view=investitionskosten_create_view, name="investitionskosten-create"),
    
]