from django.contrib import admin
from .models import TermOrSemester, PayableFee, FeePayment, FeesStructure


@admin.register(TermOrSemester)
class TermOrSemesterAdmin(admin.ModelAdmin):
    list_display = ('school', 'name', 'start_date', 'end_date', 'academic_year')
    search_fields = ('name', 'academic_year', 'school__name')


@admin.register(PayableFee)
class PayableFeeAdmin(admin.ModelAdmin):
    list_display = ('school', 'term_or_semester', 'total_fees', 'due_date')
    search_fields = ('school__name', 'term_or_semester__name', 'description')


@admin.register(FeePayment)
class FeePaymentAdmin(admin.ModelAdmin):
    list_display = ('student', 'term_or_semester', 'amount_paid', 'payment_date', 'payment_method', 'date_created', 'date_updated')
    search_fields = ('student__name', 'term_or_semester__name', 'payment_method', 'narration')
    list_filter = ('payment_method', 'payment_date')


@admin.register(FeesStructure)
class FeesStructureAdmin(admin.ModelAdmin):
    list_display = ('school', 'description', 'upload_date')
    search_fields = ('school__name', 'description')
