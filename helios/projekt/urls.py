from django.urls import path


from helios.projekt.views import (
    #Projekt
    projekt_create_view,
    projekt_list_view,
    projekt_update_view,
    projekt_delete_view,
    #ProjektSpezifikation
    projekt_createSpez_view,
    
    #Upload Stammdatencsv
    upload_file_gewerk,
    upload_file_raumnutzung,
    upload_file_gebauedenutzung, 
    upload_file_kosten_elektro,
)

app_name = "projekt"

urlpatterns = [
    #Projekt
    path("create/", view=projekt_create_view, name="create-projekt"),
    path("list/", view=projekt_list_view, name="list-projekt"),
    path("update/<int:pk>", view=projekt_update_view, name="update-projekt"),
    path("delete/", view=projekt_delete_view, name="delete-projekt"),
    #Projektspezifikation
    path("create/spez/<int:pk>", view=projekt_createSpez_view, name="create-spezprojekt"),
    
    #Upload File Stammdaten
    path('upload/gewerk', upload_file_gewerk, name = "upload-file-gewerk"),
    path('upload/raumnutzung', upload_file_raumnutzung, name = "upload-file-raumnutzung"),
    path('upload/gebauedenutzung', upload_file_gebauedenutzung, name = "upload-file-gebauedenutzung"),
    path('upload/kostenelektro', upload_file_kosten_elektro, name = "upload-file-kosten-elektro"),


]