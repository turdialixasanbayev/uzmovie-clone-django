from django.urls import path
from ..views import TagLCView, TagRUDView


urlpatterns = [
    path('tags/', TagLCView.as_view(), name='tag-list-create'),
    path('tags/<int:pk>/', TagRUDView.as_view(), name='tag-retrieve-update-destroy'),
]
