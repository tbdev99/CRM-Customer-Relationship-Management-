from django.db import models

# Create your models here.
class Tag(models.Model):
    nom=models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.nom

class Produit(models.Model):
    nom=models.CharField(max_length=50,null=True)
    prix=models.FloatField(null=True)
    tag=models.ManyToManyField(Tag,null=True)
    def __str__(self):
        return self.nom
