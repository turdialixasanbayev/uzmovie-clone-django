from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from apps.category.models import Category
from apps.category.serializers import CategoryRUDSerializer

User = get_user_model()


class CategoryRUDTestCase(APITestCase):
    """
    Test suite for Category Retrieve/Update/Delete API
    """

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword',
        )
        self.parent = Category.objects.create(name="Programming")
        self.category = Category.objects.create(
            name="Python", parent=self.parent)
        self.url = reverse('category-rud', kwargs={'slug': self.category.slug})

    def test_retrieve_category(self):
        """Kategoriya detail ko'rish"""
        response = self.client.get(self.url)

        category = Category.objects.select_related(
            "parent").get(slug=self.category.slug)
        serializer = CategoryRUDSerializer(category)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_category_authenticated(self):
        """Authlangan foydalanuvchi kategoriyani yangilaydi"""
        self.client.force_authenticate(user=self.user)
        data = {"name": "Advanced Python", "parent": self.parent.id}
        response = self.client.put(self.url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.category.refresh_from_db()
        self.assertEqual(self.category.name, "Advanced Python")

    def test_partial_update_category_authenticated(self):
        """Authlangan foydalanuvchi PATCH orqali yangilaydi"""
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(self.url, {"name": "Python 3"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.category.refresh_from_db()
        self.assertEqual(self.category.name, "Python 3")

    def test_delete_category_authenticated(self):
        """Authlangan foydalanuvchi kategoriyani o'chira oladi"""
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Category.objects.filter(
            slug=self.category.slug).exists())

    def test_unauthenticated_cannot_update_or_delete(self):
        """Authsiz foydalanuvchi faqat GET qilishi mumkin"""
        response = self.client.put(self.url, {"name": "Hack"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
