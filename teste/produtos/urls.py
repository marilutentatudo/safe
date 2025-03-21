from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('ver_produto/', views.ver_produto, name="ver_produto"),
    path('colocar_produto/', views.colocar_produto, name="colocar_produto"),

]