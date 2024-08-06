# Ingresar tus URLs de la app aquí

from django.urls import path

from . import views

app_name = "album_manager"
urlpatterns = [
    path("", views.index, name="index"),
    path("autor/", views.autors_list, name="autors_list"),
    path("album/<int:album_id>/", views.album, name="album"),
    path("add_album/", views.add_album, name="add_album"),
    path("edit_album/<int:id>/", views.edit_album, name="edit_album"),
    path("delete_album/<int:id>/", views.delete_album, name="delete_album"),
    path("autor/<int:autor_id>/", views.autor, name="autor"),
    path("autors/add_autor/", views.add_autor, name="add_autor"),
    path("autor/edit_autor/<int:autor_id>/", views.edit_autor, name="edit_autor"),
    path("autor/delete_autor/<int:autor_id>/", views.delete_autor, name="delete_autor"),
]