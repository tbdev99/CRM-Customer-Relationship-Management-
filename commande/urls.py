from django.urls import path
from . import views

urlpatterns = [
    path('',views.listCommande),
    path('nouvelle_commande/',views.ajouterCommande,name='nouvelle_commande'),
path('modifier_commande/<str:pk>/',views.modifierCommande,name='modifier_commande'),
]