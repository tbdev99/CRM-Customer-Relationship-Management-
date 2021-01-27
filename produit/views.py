from django.shortcuts import render
from django.http import  HttpResponse
from client.models import Client
from commande.models import Commande
# Create your views here.
def home(request):
    clients=Client.objects.all()
    commandes=Commande.objects.all()
    context={'clients':clients,'commandes':commandes}
    return render(request,'produit/accueil.html',context)

