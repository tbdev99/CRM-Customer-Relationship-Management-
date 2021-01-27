from django.urls import path
from . import views
urlpatterns = [
    path('<str:pk>/',views.listClients,name='client'),
    path('modifier_info_client/<str:pk>/',views.modifier_info_client,name='modifier_info_client'),
    path('nouvau_client',views.creer_client,name='nouveau_client')
]
