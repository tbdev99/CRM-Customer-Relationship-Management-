from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Client
from .forms import ClientForm
from commande.models import Commande
# Create your views here.
def listClients(request,pk):
    client=Client.objects.get(id=pk)
    commandes=client.commande_set.all()
    quantiteCommande=commandes.count()
    context={'client':client, 'commandes':commandes ,'quantiteCommandes':quantiteCommande}
    return render(request,"client/list_client.html",context)

def creer_client(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accueil')
    context = {'form': form}
    return render(request, 'client/creer_modifier_client.html', context)

def modifier_info_client(request,pk):
    client = Client.objects.get(id = pk)
    form = ClientForm(instance = client)
    if request.method=='POST':
        form=ClientForm(request.POST,instance=client)
        if form.is_valid():
            form.save()
            return redirect('accueil')
    context={'form':form}
    return render(request,'client/creer_modifier_client.html',context)
