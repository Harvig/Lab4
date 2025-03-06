from django.test import TestCase, Client
from django.urls import reverse
from main.models import Putovanje, Prijave


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

       
        self.index_url = reverse('index')
        self.register_url = reverse('register')
        self.putovanja_url = reverse('putovanja')
        self.putovanja_hr_url = reverse('putovanja_hr')
        self.putovanje_detail_url = reverse('putovanje_detail', args=[1])  
        self.add_putovanje_url = reverse('add_putovanja')
        self.update_putovanje_url = reverse('update_putovanje', args=[1]) 
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

    def test_index_GET(self):
        """Test the index view."""
        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base_generic.html')

    def test_register_GET(self):
        """Test the register view."""
        response = self.client.get(self.register_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_putovanja_GET(self):
        """Test the PutovanjeList view."""
        response = self.client.get(self.putovanja_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/putovanje_list.html')  

    def test_putovanja_hr_GET(self):
        """Test the PutovanjaCroatiaList view."""
        response = self.client.get(self.putovanja_hr_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/putovanje_list.html')  

    def test_putovanje_detail_GET(self):
        """Test the PutovanjeDetailView view."""
        response = self.client.get(self.putovanje_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/putovanje_detail.html')

    def test_add_putovanje_GET(self):
        """Test the add_putovanje view."""
        response = self.client.get(self.add_putovanje_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/form.html')

    def test_update_putovanje_GET(self):
        """Test the update_putovanje view."""
        response = self.client.get(self.update_putovanje_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/form.html')
