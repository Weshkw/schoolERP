from django.contrib import admin
from identity.models import School
from django.contrib.auth import get_user_model


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = [field.name for field in School._meta.fields]
    search_fields = [field.name for field in School._meta.fields]


@admin.register(get_user_model())
class CustomUserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in get_user_model()._meta.fields]
    search_fields = [field.name for field in get_user_model()._meta.fields]
