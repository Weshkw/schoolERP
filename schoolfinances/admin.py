from django.contrib import admin
from .models import TermOrSemester, FeeAllocationCategory, PaymentCollection, FeesStructure


@admin.register(TermOrSemester)
class TermOrSemesterAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TermOrSemester._meta.fields]
    search_fields = [field.name for field in TermOrSemester._meta.fields]


@admin.register(FeeAllocationCategory)
class FeeAllocationCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in FeeAllocationCategory._meta.fields]
    search_fields = [field.name for field in FeeAllocationCategory._meta.fields]


@admin.register(PaymentCollection)
class PaymentCollectionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PaymentCollection._meta.fields]
    search_fields = [field.name for field in PaymentCollection._meta.fields]


@admin.register(FeesStructure)
class FeesStructureAdmin(admin.ModelAdmin):
    list_display = [field.name for field in FeesStructure._meta.fields]
    search_fields = [field.name for field in FeesStructure._meta.fields]
