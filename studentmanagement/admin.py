from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    Student,
    Guardian,
    Subject,
    Grade,
    ClubsOrganization,
    Sport,
    Award
)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'national_id_or_birth_cert_name',
        'email',
        'date_of_birth',
        'address',
        'gender',
        'nationality',
        'student_identity',
        'school',
        'grade',
        'enrollment_date',
        'emergency_contact_name',
        'emergency_contact_relationship',
        'emergency_contact_phone',
        'parentguardian',
        'date_added_to_system',
        'date_updated'
    )

    search_fields = (
        'national_id_or_birth_cert_name',
        'student_identity',
        'school__name',
        'grade__name',
        'parentguardian',
        'emergency_contact_name',
        'emergency_contact_relationship',
        'emergency_contact_phone',
        'subjects__name',
        'clubs__name',
        'sports__name',
        'awards__name',
    )
    filter_horizontal = ('subjects', 'clubs', 'sports', 'awards')
    fieldsets = (
        ('Basic Information', {
            'fields': ('national_id_or_birth_cert_name','email','date_of_birth','address','gender','nationality','student_identity', 'school', 'enrollment_date')
        }),
        ('Academic Information', {
            'fields': ('grade', 'subjects')
        }),
        ('Emergency Contact', {
            'fields': ('emergency_contact_name', 'emergency_contact_relationship', 'emergency_contact_phone')
        }),
        ('Guardian Information', {
            'fields': ('parentguardian',)
        }),
        ('Extracurricular Activities', {
            'fields': ('clubs', 'sports', 'awards')
        })
    )

@admin.register(Guardian)
class GuardianAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'national_id_or_birth_cert_name',
        'email',
        'national_id_number',
        'phone_number',
        'date_joined',
        'last_login'
    )
    search_fields = (
        'username',
        'email',
        'national_id_number',
        'phone_number',
    )

    fieldsets = (
        ('Personal Information', {
            'fields': ('national_id_or_birth_cert_name','address','gender','nationality','email','national_id_number','phone_number')
        }),
        ('Dates', {
            'fields': ('date_joined', 'last_login'),
        }),
    )

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'date_created',
        'date_updated'
    )
    search_fields = (
        'id',
        'name',
        'date_created',
        'date_updated'
    )
    list_filter = ('date_created', 'date_updated')

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'date_created',
        'date_updated'
    )
    search_fields = (
        'id',
        'name',
        'date_created',
        'date_updated'
    )
    list_filter = ('date_created', 'date_updated')

@admin.register(ClubsOrganization)
class ClubsOrganizationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'date_created',
        'date_updated'
    )
    search_fields = (
        'id',
        'name',
        'date_created',
        'date_updated'
    )
    list_filter = ('date_created', 'date_updated')

@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'date_created',
        'date_updated'
    )
    search_fields = (
        'id',
        'name',
        'date_created',
        'date_updated'
    )
    list_filter = ('date_created', 'date_updated')

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'date_created',
        'date_updated'
    )
    search_fields = (
        'id',
        'name',
        'date_created',
        'date_updated'
    )
    list_filter = ('date_created', 'date_updated')