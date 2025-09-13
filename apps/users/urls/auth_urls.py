from django.urls import path
from ..views.user_lc import CustomUserLCAPIView
from ..views.user_rud import CustomUserRUDAPIView


urlpatterns = [
    path('users/', CustomUserLCAPIView.as_view(), name='user_list_create'),
    path('users/<int:pk>/', CustomUserRUDAPIView.as_view(), name='user_rud'),
]
