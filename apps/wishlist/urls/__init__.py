from django.urls import  include, path

urlpatterns = [
    path(
        '',
        include(
            'apps.wishlist.urls.wishlist_urls',
        ),
    ),
]
