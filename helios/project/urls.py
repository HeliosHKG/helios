from django.urls import path


from .views import (
    project_view,
    
)

app_name = "project"

urlpatterns = [
    path("dashboard_project/", view=project_view, name="dashboard-project"),
    
]