from django.contrib import admin

from ..models import Film, Reaction, Review, Country


admin.site.register(Film)
admin.site.register(Reaction)
admin.site.register(Review)
admin.site.register(Country)
