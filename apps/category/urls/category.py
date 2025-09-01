from django.urls import path
from ..views import CategoryLCView, CategoryRUDView


urlpatterns = [
    path("categories/", CategoryLCView.as_view(), name="category-lc"),
    path("categories/<slug:slug>/", CategoryRUDView.as_view(), name="category-rud"),
]
