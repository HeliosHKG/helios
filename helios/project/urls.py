from django.urls import path


from helios.project.views import (
    project_detail_view,
    
)

app_name = "project"
urlpatterns = [
    path("dashboard_project/", view=project_detail_view, name="dashboard-project"),
    
]