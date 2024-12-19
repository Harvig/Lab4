from django.db import models
# Create your models here.

class Putovanje(models.Model):
    putovanje_sifraPutovanja = models.IntegerField(primary_key=True)
    putovanje_naslov = models.CharField(max_length=100)
    putovanje_opis = models.TextField()
    putovanje_lokacija = models.CharField(max_length=100)
    putovanje_drzava = models.CharField(max_length=100)
    putovanje_cijena = models.DecimalField(max_digits=10, decimal_places=2)
    putovanje_datumPolaska = models.DateField()
    putovanje_brojNocenja = models.IntegerField()
    putovanje_brojOsoba = models.IntegerField()

    class Meta:
        ordering = ['putovanje_naslov']

    def __str__(self):
        return self.putovanje_naslov


class Prijave(models.Model):
    prijava_sifraPrijave = models.IntegerField(primary_key=True)
    putovanje = models.ForeignKey(Putovanje, on_delete=models.CASCADE)
    prijava_vrstaAranzmana= models.CharField(max_length=100)
    prijava_brojOsoba = models.IntegerField()

    class Meta:
        ordering = ['-prijava_sifraPrijave']

    def __str__(self):
        return self.prijava_vrstaAranzmana
    