from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CommandeForm
from .models import Commande

# Create your views here.
def listCommande(request):
    return render(request,"commande/list_commande.html")

def ajouterCommande(request):
    form=CommandeForm()
    if request.method=='POST':
        form=CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accueil')
    context={'form':form}
    return render(request,'commande/ajouter_commande.html',context)

def modifierCommande(request,pk):
    commande = Commande.objects.get(id=pk)
    form=CommandeForm(instance=commande)
    if request.method=='POST':
        form=CommandeForm(request.POST,instance=commande)
        if form.is_valid():
            form.save()
            return redirect('accueil')
    context={'form':form}
    return render(request,'commande/ajouter_commande.html',context)
def supprimerCommande(request,pk):
    commande=Commande.objects.get(id = pk)
    if request.method=='POST':
        commande.delete()
        return redirect('accueil')
    context={"commande":commande}
    return render(request,'commande/supprimer_commande.html',context)