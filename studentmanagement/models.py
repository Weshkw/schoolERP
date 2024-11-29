from django.db import models
from django.contrib.auth.hashers import make_password
from identity.models import CustomUser, School, TimeStampedModel
from django.db.models.signals import post_delete
from phonenumber_field.modelfields import PhoneNumberField
from django.dispatch import receiver

class Student(TimeStampedModel):
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text='This is where one resides, e.g., Nairobi ABC estate.'
    )

    GENDER_CHOICES = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other')
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    NATIONALITY_CHOICES = (
        ('KENYAN', 'Kenyan'),
        ('OTHERS', 'Others'),
    )
    nationality = models.CharField(max_length=100, choices=NATIONALITY_CHOICES)
    full_name = models.CharField(
        max_length=100,
        help_text='For students, provide the full name on the birth certificate.'
    )
    school = models.ForeignKey(School, on_delete=models.CASCADE, help_text="School a student attends.")
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

    # Extracurricular Activities
    student_leadership_role = models.ManyToManyField('StudentLeadershipTitle', blank=True, help_text="Name of the title, e.g., Prefect, Game Captain.")
    clubs = models.ManyToManyField('ClubsOrganization', blank=True, help_text="Clubs the student is a member of.")
    sports = models.ManyToManyField('Sport', blank=True, help_text="Sports the student participates in.")
    awards = models.ManyToManyField('Award', blank=True, help_text="Awards the student has received.")

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        unique_together = ('school', 'student_identity')

    def __str__(self):
        return self.full_name

# Signal to delete guardian if they have no more associated students
@receiver(post_delete, sender=Student)
def delete_orphaned_guardian(sender, instance, **kwargs):
    if instance.parentguardian:
        remaining_students = Student.objects.filter(parentguardian=instance.parentguardian).exists()
        if not remaining_students:
            instance.parentguardian.delete()

class Guardian(TimeStampedModel):
    guardian_user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
    )
    school = models.ManyToManyField(School, help_text="Schools a guardian has a student in.")
    national_id_number = models.CharField(
        unique=True,
        max_length=50,
        null=True,
        blank=True,
        help_text="National ID number of the guardian."
    )

    def __str__(self):
        return self.guardian_user.username

    class Meta:
        verbose_name = "Guardian"
        verbose_name_plural = "Guardians"

class Subject(TimeStampedModel):
    name = models.CharField(max_length=100, help_text="Name of the academic subject (e.g., Math, Science).")

    def __str__(self):
        return self.name

class Grade(TimeStampedModel):
    name = models.CharField(max_length=50, help_text="Educational level (e.g., Grade 1, PP1).")

    def __str__(self):
        return self.name

class StudentLeadershipTitle(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True, help_text="Name of the title, e.g., Prefect, Game Captain.")
    description = models.TextField(blank=True, null=True, help_text="Optional description of the title.")

    class Meta:
        verbose_name = "Student Leadership Title"
        verbose_name_plural = "Student Leadership Titles"

    def __str__(self):
        return self.name

class ClubsOrganization(TimeStampedModel):
    name = models.CharField(max_length=100, help_text="Name of the club or organization (e.g., Debate Club).")

    def __str__(self):
        return self.name

class Sport(TimeStampedModel):
    name = models.CharField(max_length=100, help_text="Name of the sport (e.g., Soccer, Basketball).")

    def __str__(self):
        return self.name

class Award(TimeStampedModel):
    name = models.CharField(max_length=100, help_text="Name of the award (e.g., Best Performer, Most Improved).")

    def __str__(self):
        return self.name

class Attendance(TimeStampedModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, help_text="Student whose attendance is being recorded.")
    date = models.DateField(help_text="Date of the attendance record.")
    status = models.CharField(max_length=50, choices=[('present', 'Present'), ('absent', 'Absent'), ('late', 'Late')], help_text="Attendance status.")

    def __str__(self):
        return f"{self.student.full_name} - {self.date} - {self.status}"

class ReportCard(TimeStampedModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, help_text="Student whose report card is being recorded.")
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, help_text="Grade level of the report card.")
    subjects = models.ManyToManyField(Subject, through='ReportCardSubject', help_text="Subjects and their grades in the report card.")

    def __str__(self):
        return f"{self.student.full_name} - {self.grade.name} Report Card"

class ReportCardSubject(models.Model):
    report_card = models.ForeignKey(ReportCard, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.CharField(max_length=10, help_text="Grade received in the subject.")

    def __str__(self):
        return f"{self.subject.name} - {self.grade}"

class HomeworkAssignment(TimeStampedModel):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, help_text="Subject for the homework assignment.")
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, help_text="Grade level for the homework assignment.")
    description = models.TextField(help_text="Description of the homework assignment.")
    due_date = models.DateField(help_text="Due date for the homework assignment.")

    def __str__(self):
        return f"{self.subject.name} - {self.grade.name} Homework"

class MedicalRecord(TimeStampedModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, help_text="Student whose medical record is being recorded.")
    date = models.DateField(help_text="Date of the medical record.")
    description = models.TextField(help_text="Description of the medical condition or treatment.")

    def __str__(self):
        return f"{self.student.full_name} - Medical Record - {self.date}"
