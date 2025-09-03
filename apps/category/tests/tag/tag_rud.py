from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from apps.category.models import Tag
from ...serializers import TagRUDSerializer

User = get_user_model()


class TagRUDTestCase(APITestCase):
    """
    Test suite for the Tag Retrieve/Update/Delete API endpoints.
    """

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpassword"
        )
        self.tag = Tag.objects.create(name="Python")
        self.url = reverse("tag-retrieve-update-destroy", kwargs={"pk": self.tag.pk})

    def test_unauthenticated_cannot_access(self):
        """Authsiz foydalanuvchi 403 qaytaradi"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.put(self.url, {"name": "NewName"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.patch(self.url, {"name": "PartialName"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_can_retrieve_tag(self):
        """Authlangan foydalanuvchi tagni ko'ra oladi"""
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)

        serializer = TagRUDSerializer(self.tag)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_authenticated_can_update_tag(self):
        """Authlangan foydalanuvchi tagni yangilay oladi"""
        self.client.force_authenticate(user=self.user)
        data = {"name": "Django"}
        response = self.client.put(self.url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.tag.refresh_from_db()
        self.assertEqual(self.tag.name, "Django")

    def test_authenticated_can_partial_update_tag(self):
        """Authlangan foydalanuvchi tagni PATCH bilan yangilaydi"""
        self.client.force_authenticate(user=self.user)
        data = {"name": "FastAPI"}
        response = self.client.patch(self.url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.tag.refresh_from_db()
        self.assertEqual(self.tag.name, "FastAPI")

    def test_authenticated_can_delete_tag(self):
        """Authlangan foydalanuvchi tagni o‘chirishi mumkin"""
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Tag.objects.filter(pk=self.tag.pk).exists())
