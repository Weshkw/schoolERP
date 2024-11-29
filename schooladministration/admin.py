from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Rank, Administrator, TeachingStaff, NonTeachingStaff

# Admin configuration for Rank
class RankAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_created', 'date_updated')
    search_fields = ('id', 'title')

# Admin configuration for Administrator
class AdministratorAdmin(admin.ModelAdmin):
    list_display = ('id', 'staff_user', 'get_ranks', 'professional_identity', 'national_id_number', 'date_of_joining', 'curriculum_vitae', 'get_schools', 'date_created', 'date_updated')
    search_fields = ('id', 'staff_user__username', 'professional_identity', 'national_id_number', 'date_of_joining', 'curriculum_vitae')
    filter_horizontal = ('ranks', 'school')

    def get_ranks(self, obj):
        return ", ".join([rank.title for rank in obj.ranks.all()])
    get_ranks.short_description = 'Ranks'

    def get_schools(self, obj):
        return ", ".join([school.name for school in obj.school.all()])
    get_schools.short_description = 'Schools'

# Admin configuration for TeachingStaff
class TeachingStaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'staff_user', 'get_ranks', 'professional_identity', 'national_id_number', 'date_of_joining', 'curriculum_vitae', 'school', 'get_teaching_grades', 'get_subjects', 'get_clubs', 'get_sports', 'get_awards', 'date_created', 'date_updated')
    search_fields = ('id', 'staff_user__username', 'professional_identity', 'national_id_number', 'date_of_joining', 'curriculum_vitae')
    filter_horizontal = ('ranks', 'teaching_grades', 'subjects', 'clubs', 'sports', 'awards')

    def get_ranks(self, obj):
        return ", ".join([rank.title for rank in obj.ranks.all()])
    get_ranks.short_description = 'Ranks'

    def get_teaching_grades(self, obj):
        return ", ".join([grade.name for grade in obj.teaching_grades.all()])
    get_teaching_grades.short_description = 'Teaching Grades'

    def get_subjects(self, obj):
        return ", ".join([subject.name for subject in obj.subjects.all()])
    get_subjects.short_description = 'Subjects'

    def get_clubs(self, obj):
        return ", ".join([club.name for club in obj.clubs.all()])
    get_clubs.short_description = 'Clubs'

    def get_sports(self, obj):
        return ", ".join([sport.name for sport in obj.sports.all()])
    get_sports.short_description = 'Sports'

    def get_awards(self, obj):
        return ", ".join([award.name for award in obj.awards.all()])
    get_awards.short_description = 'Awards'

# Admin configuration for NonTeachingStaff
class NonTeachingStaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'staff_user', 'get_ranks', 'professional_identity', 'national_id_number', 'date_of_joining', 'curriculum_vitae', 'school', 'get_clubs', 'get_sports', 'get_awards', 'date_created', 'date_updated')
    search_fields = ('id', 'staff_user__username', 'professional_identity', 'national_id_number', 'date_of_joining', 'curriculum_vitae')
    filter_horizontal = ('ranks', 'clubs', 'sports', 'awards')

    def get_ranks(self, obj):
        return ", ".join([rank.title for rank in obj.ranks.all()])
    get_ranks.short_description = 'Ranks'

    def get_clubs(self, obj):
        return ", ".join([club.name for club in obj.clubs.all()])
    get_clubs.short_description = 'Clubs'

    def get_sports(self, obj):
        return ", ".join([sport.name for sport in obj.sports.all()])
    get_sports.short_description = 'Sports'

    def get_awards(self, obj):
        return ", ".join([award.name for award in obj.awards.all()])
    get_awards.short_description = 'Awards'

# Register the models with the admin site
admin.site.register(Rank, RankAdmin)
admin.site.register(Administrator, AdministratorAdmin)
admin.site.register(TeachingStaff, TeachingStaffAdmin)
admin.site.register(NonTeachingStaff, NonTeachingStaffAdmin)
