from django.db import models
from django.contrib.auth.hashers import make_password
from identity.models import CustomUser, TimeStampedModel, School
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from studentmanagement.models import ClubsOrganization, Sport, Award, Grade, Subject

class Rank(TimeStampedModel):
    title = models.CharField(
        max_length=255,
        help_text="This is the rank anyone holds in school, e.g., principal, deputy principal, headteacher, etc."
    )

    def __str__(self):
        return self.title

class BaseStaff(TimeStampedModel):
    staff_user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )
    ranks = models.ManyToManyField(
        Rank,
        help_text="Staff's ranks within the school"
    )
    professional_identity = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="Professional identifier assigned by an organization, e.g., TSC number for teachers."
    )
    national_id_number = models.CharField(
        max_length=50,
        unique=True,
        error_messages={
            'unique': _('This National ID number is already registered in the system.')
        }
    )
    date_of_joining = models.DateField(
        help_text="Date the administrator joined the school."
    )
    curriculum_vitae = models.FileField(upload_to='curriculum_vitae/', null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        rank_titles = ", ".join(rank.title for rank in self.ranks.all())
        return f"{self.staff_user.national_id_or_birth_cert_name} - {rank_titles}"

    def clean(self):
        if self.curriculum_vitae:
            ext = self.curriculum_vitae.name.split('.')[-1].lower()
            if ext != 'pdf':
                raise ValidationError("Only PDF files are allowed. Ensure you convert the file you want to upload to PDF")

class Administrator(BaseStaff):
    school = models.ManyToManyField(School, help_text="School a staff works for.",related_name='administrator_profile')

    class Meta:
        verbose_name = "Administrator"
        verbose_name_plural = "Administrators"

class TeachingStaff(BaseStaff):
    school = models.ForeignKey(School, on_delete=models.CASCADE, help_text="School a staff works for.",related_name='teaching_staff_profile')
    teaching_grades = models.ManyToManyField(
        Grade,
        help_text="The grade levels taught by the teacher."
    )
    subjects = models.ManyToManyField(
        Subject,
        help_text="The subjects the teacher specializes in."
    )
    clubs = models.ManyToManyField(
        ClubsOrganization,
        blank=True,
        help_text="The clubs mentored by the teacher."
    )
    sports = models.ManyToManyField(
        Sport,
        blank=True,
        help_text="The sports coached or guided by the teacher."
    )
    awards = models.ManyToManyField(
        Award,
        blank=True,
        help_text="The awards received by the teacher."
    )

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

class NonTeachingStaff(BaseStaff):
    school = models.ForeignKey(School, on_delete=models.CASCADE, help_text="School a staff works for.",related_name='non_teaching_staff_profile')
    clubs = models.ManyToManyField(
        ClubsOrganization,
        blank=True,
        help_text="The clubs the non-teaching staff member is part of."
    )
    sports = models.ManyToManyField(
        Sport,
        blank=True,
        help_text="The sports the non-teaching staff member is involved in."
    )
    awards = models.ManyToManyField(
        Award,
        blank=True,
        help_text="The awards received by the non-teaching staff member."
    )

    class Meta:
        verbose_name = "Non-Teaching Staff"
        verbose_name_plural = "Non-Teaching StaffS"
