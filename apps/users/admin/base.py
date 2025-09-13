from django.contrib import admin
from django.contrib.auth.models import Group


admin.site.site_header = "Uzmovie Admin Panel"
admin.site.site_title = "Uzmovie Admin Panel"
admin.site.index_title = "Welcome to Uzmovie Admin Panel"
admin.site.empty_value_display = "Not available"


admin.site.unregister(Group)
