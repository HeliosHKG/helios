from django.urls import path


from .views import (
    projekt_create_view,
    
)

app_name = "project"

urlpatterns = [
    path("create/", view=projekt_create_view, name="create-projekt"),
    
]