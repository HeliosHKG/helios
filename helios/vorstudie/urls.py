from django.urls import path


from helios.project.views import (
    vorstudie_detail_view,
    
)

app_name = "vorstudie"
urlpatterns = [
    path("dashboard_vorstudie/", view=vorstudie_detail_view, name="dashboard-project"),
    
]