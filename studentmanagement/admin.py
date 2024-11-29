from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import (
    Student, Guardian, Subject, Grade, StudentLeadershipTitle,
    ClubsOrganization, Sport, Award, Attendance, ReportCard,
    ReportCardSubject, HomeworkAssignment, MedicalRecord
)

# Admin configuration for Student
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'full_name', 'date_of_birth', 'address', 'gender', 'nationality',
        'school', 'student_identity', 'enrollment_date', 'emergency_contact_name',
        'emergency_contact_relationship', 'emergency_contact_phone', 'parentguardian',
        'get_subjects', 'grade', 'get_student_leadership_roles', 'get_clubs', 'get_sports', 'get_awards',
        'date_created', 'date_updated'
    )
    search_fields = (
        'id', 'full_name', 'date_of_birth', 'address', 'gender', 'nationality',
        'school__name', 'student_identity', 'enrollment_date', 'emergency_contact_name',
        'emergency_contact_relationship', 'emergency_contact_phone', 'parentguardian__guardian_user__username',
        'subjects__name', 'grade__name', 'student_leadership_role__name', 'clubs__name', 'sports__name', 'awards__name'
    )
    filter_horizontal = ('subjects', 'student_leadership_role', 'clubs', 'sports', 'awards')

    def get_subjects(self, obj):
        return ", ".join([subject.name for subject in obj.subjects.all()])
    get_subjects.short_description = 'Subjects'

    def get_student_leadership_roles(self, obj):
        return ", ".join([role.name for role in obj.student_leadership_role.all()])
    get_student_leadership_roles.short_description = 'Student Leadership Roles'

    def get_clubs(self, obj):
        return ", ".join([club.name for club in obj.clubs.all()])
    get_clubs.short_description = 'Clubs'

    def get_sports(self, obj):
        return ", ".join([sport.name for sport in obj.sports.all()])
    get_sports.short_description = 'Sports'

    def get_awards(self, obj):
        return ", ".join([award.name for award in obj.awards.all()])
    get_awards.short_description = 'Awards'

# Admin configuration for Guardian
class GuardianAdmin(admin.ModelAdmin):
    list_display = ('id', 'guardian_user', 'get_schools', 'national_id_number', 'date_created', 'date_updated')
    search_fields = ('id', 'guardian_user__username', 'national_id_number')
    filter_horizontal = ('school',)

    def get_schools(self, obj):
        return ", ".join([school.name for school in obj.school.all()])
    get_schools.short_description = 'Schools'

# Admin configuration for Subject
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_created', 'date_updated')
    search_fields = ('id', 'name')

# Admin configuration for Grade
class GradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_created', 'date_updated')
    search_fields = ('id', 'name')

# Admin configuration for StudentLeadershipTitle
class StudentLeadershipTitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'date_created', 'date_updated')
    search_fields = ('id', 'name', 'description')

# Admin configuration for ClubsOrganization
class ClubsOrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_created', 'date_updated')
    search_fields = ('id', 'name')

# Admin configuration for Sport
class SportAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_created', 'date_updated')
    search_fields = ('id', 'name')

# Admin configuration for Award
class AwardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_created', 'date_updated')
    search_fields = ('id', 'name')

# Admin configuration for Attendance
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'date', 'status', 'date_created', 'date_updated')
    search_fields = ('id', 'student__full_name', 'date', 'status')

# Admin configuration for ReportCard
class ReportCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'grade', 'get_subjects', 'date_created', 'date_updated')
    search_fields = ('id', 'student__full_name', 'grade__name', 'subjects__name')
    filter_horizontal = ('subjects',)

    def get_subjects(self, obj):
        return ", ".join([subject.name for subject in obj.subjects.all()])
    get_subjects.short_description = 'Subjects'

# Admin configuration for ReportCardSubject
class ReportCardSubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'report_card', 'subject', 'grade')
    search_fields = ('id', 'report_card__student__full_name', 'subject__name', 'grade')

# Admin configuration for HomeworkAssignment
class HomeworkAssignmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'grade', 'description', 'due_date', 'date_created', 'date_updated')
    search_fields = ('id', 'subject__name', 'grade__name', 'description', 'due_date')

# Admin configuration for MedicalRecord
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'date', 'description', 'date_created', 'date_updated')
    search_fields = ('id', 'student__full_name', 'date', 'description')

# Register the models with the admin site
admin.site.register(Student, StudentAdmin)
admin.site.register(Guardian, GuardianAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(StudentLeadershipTitle, StudentLeadershipTitleAdmin)
admin.site.register(ClubsOrganization, ClubsOrganizationAdmin)
admin.site.register(Sport, SportAdmin)
admin.site.register(Award, AwardAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(ReportCard, ReportCardAdmin)
admin.site.register(ReportCardSubject, ReportCardSubjectAdmin)
admin.site.register(HomeworkAssignment, HomeworkAssignmentAdmin)
admin.site.register(MedicalRecord, MedicalRecordAdmin)
