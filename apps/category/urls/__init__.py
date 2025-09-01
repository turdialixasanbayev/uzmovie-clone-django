from django.urls import path, include


urlpatterns = [
    path('', include('apps.category.urls.category')),
]
