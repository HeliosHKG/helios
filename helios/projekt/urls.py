from django.urls import path


from .views import (
    projekt_create_view,
    projekt_list_view,
    projekt_update_view,
    projekt_delete_view,
)

app_name = "projekt"

urlpatterns = [
    path("create/", view=projekt_create_view, name="create-projekt"),
    path("list/", view=projekt_list_view, name="list-projekt"),
    path("update/", view=projekt_update_view, name="update-projekt"),
    path("delete/", view=projekt_delete_view, name="delete-projekt"),

]