from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import (
    index,
    register,
    PutovanjeList,
    PrijaveList,
    PutovanjaCroatiaList,
    PutovanjeDetailView,
    add_putovanje,
    update_putovanje
)

print("Test file loaded!")

class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)

    def test_putovanja_url_is_resolved(self):
        url = reverse('putovanja')
        self.assertEquals(resolve(url).func.view_class, PutovanjeList)

    def test_prijave_url_is_resolved(self):
        url = reverse('prijave')
        self.assertEquals(resolve(url).func.view_class, PrijaveList)

    def test_putovanja_hr_url_is_resolved(self):
        url = reverse('putovanja_hr')
        self.assertEquals(resolve(url).func.view_class, PutovanjaCroatiaList)

    def test_putovanje_detail_url_is_resolved(self):
        url = reverse('putovanje_detail', args=[1])  
        self.assertEquals(resolve(url).func.view_class, PutovanjeDetailView)

    def test_add_putovanja_url_is_resolved(self):
        url = reverse('add_putovanja')
        self.assertEquals(resolve(url).func, add_putovanje)

    def test_update_putovanje_url_is_resolved(self):
        url = reverse('update_putovanje', args=[1])  
        self.assertEquals(resolve(url).func, update_putovanje)
