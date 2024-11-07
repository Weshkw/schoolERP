from django.contrib import admin
from .models import Administrator, AdministratorRank

class AdministratorAdmin(admin.ModelAdmin):
    model = Administrator
    list_display = (
        'national_id_or_birth_cert_name','get_ranks','professional_identity','phone_number','national_id_number','email', 'date_of_birth','gender', 'nationality', 'school','date_of_joining', 'is_staff'
    )

    filter_horizontal = ('ranks',)
    fieldsets = (
        ('Basic Information', {
            'fields': ( 'national_id_or_birth_cert_name','national_id_number', 'email')
        }),
        ('Personal Details', {
            'fields': ('phone_number','address', 'gender', 'nationality', 'date_of_birth'),
            'description': 'Provide basic personal information for the administrator.'
        }),
        ('Employment Details', {
            'fields': ('school', 'ranks','professional_identity', 'date_of_joining'),
            'description': 'Specify the administrator’s employment-related information.'
        }),
        ('Permissions', {
            'fields': ('is_staff',),
            'description': 'Set the administrator’s access permissions.'
        }),
    )
    search_fields = ('username', 'email', 'national_id_or_birth_cert_name')
    ordering = ('username',)

    def get_ranks(self, obj):
        return ", ".join(rank.title for rank in obj.ranks.all())
    get_ranks.short_description = 'Ranks'

# Register AdministratorRank separately
admin.site.register(Administrator, AdministratorAdmin)
admin.site.register(AdministratorRank)
