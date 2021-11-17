from django.urls import path


from .views import (
    #Projekt
    projekt_create_view,
    projekt_list_view,
    projekt_update_view,
    projekt_delete_view,
    #ProjektSpezifikation
    projekt_createSpez_view
)

app_name = "projekt"

urlpatterns = [
    #Projekt
    path("create/", view=projekt_create_view, name="create-projekt"),
    path("list/", view=projekt_list_view, name="list-projekt"),
    path("update/", view=projekt_update_view, name="update-projekt"),
    path("delete/", view=projekt_delete_view, name="delete-projekt"),
    #Projektspezifikation
    path("create/spez/<int:pk>", view=projekt_createSpez_view, name="create-spezprojekt"),
    

]