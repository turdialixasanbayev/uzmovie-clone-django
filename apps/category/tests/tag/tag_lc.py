from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from apps.category.models import Tag
from ...serializers import TagLCSerializer

User = get_user_model()


class TagLCTestCase(APITestCase):
    """
    Test suite for the Tag List/Create API endpoints.
    """

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('tag-list-create')
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword',
        )
        self.tag = Tag.objects.create(name="Python")

    def test_unauthenticated_cannot_access(self):
        """Authsiz foydalanuvchi uchun 403 qaytishi kerak"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.post(self.url, {"name": "DRF"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_can_list_tags(self):
        """Authlangan foydalanuvchi ro'yxatni ko'radi"""
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)

        tags = Tag.objects.all().order_by("name")
        serializer = TagLCSerializer(tags, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Paginatsiya sababli faqat results qismi bilan solishtiramiz
        self.assertEqual(response.data["results"], serializer.data)

    def test_authenticated_can_create_tag(self):
        """Authlangan foydalanuvchi yangi tag yaratadi"""
        self.client.force_authenticate(user=self.user)
        data = {"name": "DRF"}
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Tag.objects.filter(name="DRF").exists())

    def test_filter_tags(self):
        """Filter ishlashini tekshirish"""
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url, {"name": "Python"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Paginatsiya sabab results ichidan tekshiramiz
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["name"], "Python")
