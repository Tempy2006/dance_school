from django.contrib import admin
from .models import School


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "street", "phone", "email")
    search_fields = ("name", "city")
