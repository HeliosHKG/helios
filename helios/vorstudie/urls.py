from django.urls import path


from .views import (
    vorstudie_view,
    
)

app_name = "vorstudie"
urlpatterns = [
    path("dashboard_vorstudie/", view=vorstudie_view, name="dashboard-project"),
    
]