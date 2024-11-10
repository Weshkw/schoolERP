from django.db import models
from django.contrib.auth.hashers import make_password
from identity.models import CustomUser, School
from django.db.models.signals import post_delete
from phonenumber_field.modelfields import PhoneNumberField
from django.dispatch import receiver


class Student(CustomUser):
    school = models.ForeignKey(School, on_delete=models.CASCADE, help_text="School where the student is enrolled.")
    student_identity = models.CharField(
        max_length=255,
        help_text="Unique student identifier in the school (e.g., Admission number)."
    )
    enrollment_date = models.DateField(help_text="Date the student was admitted into the school.")

    # Emergency Contact Information
    emergency_contact_name = models.CharField(max_length=255, help_text="Name of the student's emergency contact.")
    EMERGENCY_CONTACT_RELATIONSHIP_CHOICES = [
        ('parent or guardian', 'Parent or Guardian'),
        ('uncle', 'Uncle'),
        ('aunt', 'Aunt'),
        ('grandparent', 'Grandparent'),
        ('cousin', 'Cousin'),
        ('trusted family friend', 'Trusted Family Friend'),
    ]
    emergency_contact_relationship = models.CharField(
        max_length=100,
        choices=EMERGENCY_CONTACT_RELATIONSHIP_CHOICES,
        help_text="Relationship between the emergency contact and the student."
    )
    emergency_contact_phone = PhoneNumberField(
        help_text="Phone number of the emergency contact, preferably someone who can respond quickly in emergencies."
    )

    parentguardian = models.ForeignKey(
        'Guardian',
        on_delete=models.SET_NULL,
        null=True,
        help_text="Parent or guardian associated with the student."
    )

    # Academic Information
    subjects = models.ManyToManyField('Subject', blank=True, help_text="Subjects the student is taking.")
    grade = models.ForeignKey(
        'Grade',
        on_delete=models.SET_NULL,
        null=True,
        help_text="Current grade level of the student."
    )
    date_added_to_system = models.DateField(auto_now_add=True, help_text="Date the student was added to the system.")
    date_updated = models.DateTimeField(auto_now=True, help_text="Date the student's record was last updated.")

    # Extracurricular Activities
    clubs = models.ManyToManyField('ClubsOrganization', blank=True, help_text="Clubs the student is a member of.")
    sports = models.ManyToManyField('Sport', blank=True, help_text="Sports the student participates in.")
    awards = models.ManyToManyField('Award', blank=True, help_text="Awards the student has received.")

    def save(self, *args, **kwargs):
        # Set the username to student_identity and password to the grade name before saving.
        self.username = self.student_identity
        self.password = make_password(self.grade.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return self.national_id_or_birth_cert_name


# Signal to delete guardian if they have no more associated students
@receiver(post_delete, sender=Student)
def delete_orphaned_guardian(sender, instance, **kwargs):
    if instance.parentguardian:
        remaining_students = Student.objects.filter(parentguardian=instance.parentguardian).exists()
        if not remaining_students:
            instance.parentguardian.delete()


class Guardian(CustomUser):
    national_id_number = models.CharField(
        unique=True,
        max_length=50,
        null=True,
        blank=True,
        help_text="National ID number of the guardian."
    )
    phone_number = PhoneNumberField(
        unique=True,
        help_text="Phone number for identifying and contacting the guardian."
    )
    date_created = models.DateField(auto_now_add=True, help_text="Date the guardian was added to the system.")
    date_updated = models.DateTimeField(auto_now=True, help_text="Date the guardian's record was last updated.")

    def __str__(self):
        return self.national_id_or_birth_cert_name

    def save(self, *args, **kwargs):
        # Set the username to phone_number and password to the phone number before saving.
        self.username = self.phone_number
        self.password = make_password(str(self.phone_number))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Guardian"
        verbose_name_plural = "Guardians"


class Subject(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the academic subject (e.g., Math, Science).")
    date_created = models.DateField(auto_now_add=True, help_text="Date the subject was created.")
    date_updated = models.DateTimeField(auto_now=True, help_text="Date the subject's record was last updated.")

    def __str__(self):
        return self.name


class Grade(models.Model):
    name = models.CharField(max_length=50, help_text="Educational level (e.g., Grade 1, PP1).")
    date_created = models.DateField(auto_now_add=True, help_text="Date the grade was created.")
    date_updated = models.DateTimeField(auto_now=True, help_text="Date the grade's record was last updated.")

    def __str__(self):
        return self.name


class ClubsOrganization(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the club or organization (e.g., Debate Club).")
    date_created = models.DateField(auto_now_add=True, help_text="Date the club or organization was created.")
    date_updated = models.DateTimeField(auto_now=True, help_text="Date the club or organization's record was last updated.")

    def __str__(self):
        return self.name


class Sport(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the sport (e.g., Soccer, Basketball).")
    date_created = models.DateField(auto_now_add=True, help_text="Date the sport was added.")
    date_updated = models.DateTimeField(auto_now=True, help_text="Date the sport's record was last updated.")

    def __str__(self):
        return self.name


class Award(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the award (e.g., Best Performer, Most Improved).")
    date_created = models.DateField(auto_now_add=True, help_text="Date the award was added.")
    date_updated = models.DateTimeField(auto_now=True, help_text="Date the award's record was last updated.")

    def __str__(self):
        return self.name
    
class Attendance(models.Model):
    pass

class ReportCard(models.Model):
    pass

class HomeworkAssignment(models.Model):
    pass
class MedicalRecord(models.Model):
    pass