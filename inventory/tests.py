from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Item
from django.contrib.auth.models import User

# Create your tests here.

class ItemAPITests(APITestCase):

    def setUp(self):
        print("[INFO] Test starting.")
        self.user = User.objects.create_user(username='test_user',password='test12345')
        self.client.login(username='test_user',password='test12345')

        url = reverse('token_obtain_pair')
        response = self.client.post(url, {'username':'test_user','password':'test12345'}, format='json')
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        self.item = Item.objects.create(name='laptop', description='Gaming laptop', item_id='LP1234',price=67000, quantity=17)
        self.create_url = reverse('create_item')
        self.detail_url = reverse('item_detail',args=[self.item.id])

    def tearDown(self):
        print("[INFO] Test finished.")
    
    def test_create_item(self):
        """
        Item creation test.
        """

        data = {
            'name': 'Laptop',
            'description': 'A High performance gaming laptop.',
            'item_id': 'LP0011',
            'price': '78999.00',
            'quantity': 11
        }

        response = self.client.post(self.create_url, data, format='json')
        # print("create item :: ",response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print('[INFO] Test create item ended.')

    def test_get_all_items(self):
        """
        Test to get all items
        """
        url = reverse('list_items')
        response = self.client.get(url, format='json')
        # print("get all items :: ",response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_item(self):    
        """
        Test to get a signle item.
        """
        response = self.client.get(self.detail_url, format='json')
        # print("Get single item :: ",response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_item(self):
        """
        Test to update an existing data.
        """
        update_data = {
            'name': 'Laptop',
            'description': 'A High performance gaming laptop.',
            'item_id': 'LP1234',
            'price': '78999.00',
            'quantity': 11
        }
        response = self.client.put(self.detail_url,update_data,format='json')
        # print(response.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['name'],'Laptop')


    def test_delete_item(self):
        """
        Test to delete item.
        """
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_access_without_token(self):
        """
        Negative test to check working of authentication.
        """
        self.client.credentials()
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    


    
        
