from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from apps.findings.models import (
    Finding, 
    Category
)
from apps.users.models import User


class FindingTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username = 'test',
            email = 'test@gmail.com',
            number = '+996704025833',
            password = '123123',
        )
        self.category = Category.objects.create(name = 'post')
      

 
    def test_getting_findings_list(self):
        finding_1 = Finding.objects.create(
            name='finding_1',
            description='finding_1',
            price='100',
            author = self.user,
            category=self.category,
        )
        finding_2 = Finding.objects.create(
            name='finding_2',
            description='finding_2',
            price='100',
            author=self.user,
            category=self.category,
        )
        response = self.client.get(reverse('findings'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)
        self.assertEqual(response.json()[0]['id'], str(finding_1.id))
        self.assertEqual(response.json()[1]['id'], str(finding_2.id))

    
    def test_create_finding(self):
        data = {
            'name': 'test_finding',
            'description': 'finding_2',
            'price': '200', 
            'author': str(self.user_id),
            'category': str(self.category_id)
        }
        response = self.client.post(reverse('finding-create'), data=data )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['id'])
        response = response.json().pop('id')
        self.assertEqual(response.json(), data)
        