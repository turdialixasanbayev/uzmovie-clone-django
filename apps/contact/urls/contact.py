from django.urls import path, include
from apps.contact.views import ContactViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'contacts', ContactViewSet, basename='contacts')


urlpatterns = [
    path('', include(router.urls)),
]
