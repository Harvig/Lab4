from django.test import TestCase
from main.models import Putovanje, Prijave


class TestModels(TestCase):

    def setUp(self):
        self.putovanje1 = Putovanje.objects.create(
            putovanje_sifraPutovanja=1,
            putovanje_naslov="Adriatic Adventure",
            putovanje_opis="A wonderful trip along the Adriatic coast.",
            putovanje_lokacija="Dubrovnik",
            putovanje_drzava="Croatia",
            putovanje_cijena=1500.00,
            putovanje_datumPolaska="2025-06-15",
            putovanje_brojNocenja=7,
            putovanje_brojOsoba=2
        )

        self.prijava1 = Prijave.objects.create(
            prijava_sifraPrijave=101,
            putovanje=self.putovanje1,
            prijava_vrstaAranzmana="All-Inclusive",
            prijava_brojOsoba=2
        )

    def test_putovanje_creation(self):
        """Test that the Putovanje instance is created correctly."""
        self.assertEquals(self.putovanje1.putovanje_naslov, "Adriatic Adventure")
        self.assertEquals(self.putovanje1.putovanje_lokacija, "Dubrovnik")
        self.assertEquals(self.putovanje1.putovanje_cijena, 1500.00)
        self.assertEquals(self.putovanje1.putovanje_brojNocenja, 7)

    def test_prijave_creation(self):
        """Test that the Prijave instance is created correctly."""
        self.assertEquals(self.prijava1.prijava_sifraPrijave, 101)
        self.assertEquals(self.prijava1.prijava_vrstaAranzmana, "All-Inclusive")
        self.assertEquals(self.prijava1.prijava_brojOsoba, 2)
        self.assertEquals(self.prijava1.putovanje, self.putovanje1)

    def test_putovanje_str_method(self):
        """Test the __str__ method of the Putovanje model."""
        self.assertEquals(str(self.putovanje1), "Adriatic Adventure")

    def test_prijave_str_method(self):
        """Test the __str__ method of the Prijave model."""
        self.assertEquals(str(self.prijava1), "All-Inclusive")
