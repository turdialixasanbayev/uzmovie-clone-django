from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from apps.category.models import Category
from apps.category.serializers import CategoryLCSerializer

User = get_user_model()


class CategoryLCTestCase(APITestCase):
    """
    Test suite for Category List/Create API
    """

    def setUp(self):
        self.client = APIClient()
        self.url = reverse("category-lc")

        # Test user
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpassword",
        )

        # Categories
        self.parent = Category.objects.create(name="Programming")
        self.child = Category.objects.create(name="Python", parent=self.parent)

    def test_unauthenticated_cannot_access(self):
        """Authsiz foydalanuvchi uchun 403 qaytishi kerak"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.post(self.url, {"name": "Django"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_can_list_categories(self):
        """Authlangan foydalanuvchi kategoriyalarni ko'ra oladi"""
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)

        categories = Category.objects.select_related("parent").all().order_by("name")
        serializer = CategoryLCSerializer(categories, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_authenticated_can_create_category(self):
        """Authlangan foydalanuvchi yangi kategoriya yaratadi"""
        self.client.force_authenticate(user=self.user)
        data = {"name": "Django", "parent": self.parent.id}
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(
            Category.objects.filter(name="Django", parent=self.parent).exists()
        )

    def test_filter_categories_by_name(self):
        """Kategoriya name bo'yicha filter ishlaydi"""
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url, {"name": "Python"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Python")

    def test_filter_categories_by_parent(self):
        """Kategoriya parent bo'yicha filter ishlaydi"""
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url, {"parent": self.parent.id})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Python")
