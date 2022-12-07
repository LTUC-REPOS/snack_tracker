from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack

class SnacksTest(TestCase):

    def tests_home_page_status(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    def tests_about_page_status(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    def test_home_page(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')


    def test_about_page(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')


    def setUp(self):
            self.user= get_user_model().objects.create_user(
                username='test',
                email='test@test.com',
                password='123'
            )
            self.Snack=Snack.objects.create(
                name='test',
                purchaser=self.user,
                description='test'

            )


    def test_snack_detail(self):
            url= reverse('snack',kwargs={'pk':self.Snack.pk})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)


    def test_snack_page(self):
        url= reverse('snack',kwargs={'pk':self.Snack.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_detail.html')