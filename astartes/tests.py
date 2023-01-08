from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
# Create your tests here.
from django.contrib.auth import get_user_model
from .models import Marine


from django.urls import reverse


class MarineTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        testuser2 = get_user_model().objects.create_user(
            username="testuser2", password="pass"
        )
        testuser2.save()

        test_astartes = Marine.objects.create(
            title="rake",
            region=testuser1,
            description="Better for collecting leaves than a shovel.",
        )
        test_astartes.save()

    def setUp(self):
        self.client.login(username='testuser1', password="pass")

    def test_astartes_model(self):
        marine = Marine.objects.get(id=1)
        actual_region = str(marine.region)
        actual_name = str(marine.title)
        actual_description = str(marine.description)
        self.assertEqual(actual_region, "testuser1")
        self.assertEqual(actual_name, "rake")
        self.assertEqual(
            actual_description, "Better for collecting leaves than a shovel."
        )

    def test_get_marine_list(self):
        url = reverse("marine_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        Marine = response.data
        self.assertEqual(len(Marine), 1)

    def test_auth_required(self):
        self.client.logout()
        url = reverse("marine_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_only_owner_can_delete(self):
        self.client.logout()
        self.client.login(username='testuser2', password="pass")
        url = reverse("marine_detail", args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)