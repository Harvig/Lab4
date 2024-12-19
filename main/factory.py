import factory
from factory.django import DjangoModelFactory
from main.models import *


class PutovanjeFactory(DjangoModelFactory):
    class Meta:
        model = Putovanje


    putovanje_sifraPutovanja = factory.Sequence(lambda n: n + 1)  
    putovanje_naslov = factory.Faker("sentence", nb_words=3)  
    putovanje_opis = factory.Faker("text", max_nb_chars=200) 
    putovanje_lokacija = factory.Faker("city")  
    putovanje_drzava = factory.Faker("country")
    putovanje_cijena = factory.Faker("pydecimal", left_digits=6, right_digits=2, positive=True)
    putovanje_datumPolaska = factory.Faker("date_between", start_date="today", end_date="+1y")
    putovanje_brojNocenja = factory.Faker("random_int", min=1, max=14)
    putovanje_brojOsoba = factory.Faker("random_int", min=1, max=60)


class PrijaveFactory(DjangoModelFactory):
    class Meta:
        model = Prijave

    prijava_sifraPrijave = factory.Sequence(lambda n: n + 1)  
    putovanje = factory.SubFactory(PutovanjeFactory)  
    prijava_vrstaAranzmana = factory.Faker("word")
    prijava_brojOsoba = factory.Faker("random_int", min=1, max=5)
