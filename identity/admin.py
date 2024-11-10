from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, School

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = (
        'username',
        'email',
        'national_id_or_birth_cert_name',
        'date_of_birth',
        'gender',
        'nationality',
        'address',
        'is_active',
        'is_staff',
        'date_joined',
        'last_login'
    )
    
    search_fields = (
        'username',
        'email',
        'national_id_or_birth_cert_name',
        'address',
        'gender',
        'nationality'
    )
    
    list_filter = (
        'is_active',
        'is_staff',
        'is_superuser',
        'gender',
        'nationality',
        'date_joined',
        'last_login'
    )
    
    fieldsets = (
        ('Personal Info', {
            'fields': (
                'username',
                'email',
                'password',
                'national_id_or_birth_cert_name',
                'date_of_birth',
                'gender',
                'nationality',
                'address'
            )
        }),
        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions'
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'email',
                'password1',
                'password2',
                'national_id_or_birth_cert_name',
                'date_of_birth',
                'gender',
                'nationality',
                'address',
                'is_active',
                'is_staff',
                'is_superuser'
            ),
        }),
    )
    
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'principal_name',
        'school_type',
        'contact_number',
        'email',
        'established_date',
        'date_created',
        'date_updated'
    )
    
    search_fields = (
        'name',
        'school_identity',
        'principal_name',
        'address',
        'contact_number',
        'email'
    )
    
    list_filter = (
        'school_type',
        'established_date',
        'date_created',
        'date_updated'
    )
    
    fieldsets = (
        ('Basic Information', {
            'fields': (
                'name',
                'id',
                'school_type',
                'established_date'
            )
        }),
        ('Contact Information', {
            'fields': (
                'address',
                'contact_number',
                'email'
            )
        }),
        ('Administration', {
            'fields': (
                'principal_name',
            )
        }),
    )
    
    readonly_fields = ('id', 'date_created', 'date_updated')