from django.urls import reverse, include, resolve
from django.test import SimpleTestCase



class ApiUrlsTests(SimpleTestCase):

    def test_get_customers_is_resolved(self):
        url = reverse('customer')
        print(url)
        


