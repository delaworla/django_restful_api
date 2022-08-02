from django.urls import reverse, include, resolve
from django.test import SimpleTestCase
from api.views import CustomerView
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.views import APIView




class ApiUrlsTests(SimpleTestCase):

    def test_get_customers_is_resolved(self):
        url = reverse('customer')
        self.assertEquals(resolve(url).func.view_class, CustomerView)
    
    
class CustomerAPIViewTests(APITestCase):
    customers_url = reverse("customer")

    def setUp(self):
        self.user = User.objects.create_user(
            username='admin', password='django')
        self.token = Token.objects.create(user=self.user)
        #self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_customers_authenticated(self):
        response = self.client.get(self.customers_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_customers_un_authenticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(self.customers_url)
        self.assertEquals(response.status_code, 401)

