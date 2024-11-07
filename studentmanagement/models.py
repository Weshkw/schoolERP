from django.db import models
from django.contrib.auth.hashers import make_password
from identity.models import CustomUser,School
from django.db.models.signals import post_delete
from phonenumber_field.modelfields import PhoneNumberField
from django.dispatch import receiver

class Student(CustomUser):
    #Student can only be at one school at a time
    school= models.ForeignKey(School,on_delete=models.CASCADE)
    student_identity=models.CharField(max_length=255,help_text='Eg Admission number of a student or any other unique identity of a student in the school.')
    enrollment_date = models.DateField(help_text='This is the date the student was admitted into the school.')

    # Contact Information
    emergency_contact_name = models.CharField(max_length=255)
    EMERGENCY_CONTACT_RELATIONSHIP_CHOICES = (
        ('parent or guardian', 'PARENT OR GUARDIAN'),
        ('uncle', 'UNCLE'),
        ('aunt', 'AUNT'),
        ('grandparent', 'GRANDPARENT'),
        ('cousin', 'COUSIN'),
        ('trusted family friend', 'TRUSTED FAMILY FRIEND'),
    )
    emergency_contact_relationship = models.CharField(
        max_length=100, choices=EMERGENCY_CONTACT_RELATIONSHIP_CHOICES
    )
    emergency_contact_phone = PhoneNumberField(
        help_text="The emergency contact should be someone who is easily reachable by phone and has a close relationship with the student so they can respond quickly during emergencies. ",
    )

    # A student can only have one parent or guardian associated with them.Reason for setting null is because a parent might be having other students
    parentguardian = models.ForeignKey('Guardian', on_delete=models.SET_NULL, null=True, help_text='Can be parent or guardian.')

    # Academic Information
    # A student can take as many subjects as they want, and each subject can have many students.
    subjects = models.ManyToManyField('Subject', blank=True)
    # A student can only be enrolled in one grade level at a time. No student can be in multiple grades simultaneously.
    grade = models.ForeignKey('Grade', on_delete=models.SET_NULL, null=True, help_text='Level of education a student is currently in.')
    date_added_to_system = models.DateField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    # Extracurricular Activities
    # A student can join multiple clubs, and a club can have many students as members.
    clubs = models.ManyToManyField('ClubsOrganization', blank=True)
    # A student can participate in multiple sports, and a sport can have many students participating.
    sports = models.ManyToManyField('Sport', blank=True)
    # A student can earn multiple awards, and an award can be given to multiple students.
    awards = models.ManyToManyField('Award', blank=True)

    def save(self, *args, **kwargs):
        # Set the username to student_idintity and password to grade.name before saving. Onbording manual should advise students to cahange password of their accounts once they start using the account
        self.username = self.student_identity
        self.password=make_password(self.grade.name)
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
    national_id_number = models.CharField(unique=True, max_length=50,null=True,blank=True, )
    phone_number = PhoneNumberField(
        unique=True,
        help_text="A parent's phone number helps match them with the right student, even if two parents have similar names. No two parents can have the same phone numbers.",
    )
    date_created=models.DateField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.national_id_or_birth_cert_name
    
    def save(self, *args, **kwargs):
        # Set the username to student_id before saving
        self.username = self.phone_number
        self.password=make_password(F'{self.phone_number}')
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Guardian"
        verbose_name_plural = "Guardians"

   

class Subject(models.Model):
    # A subject represents the academic disciplines a student takes, such as Math, Science, etc.
    name = models.CharField(max_length=100)
    date_created=models.DateField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Grade(models.Model):
    # A grade represents the student's educational level, such as Grade 1, Grade 2, PP1, PP2, etc.
    name = models.CharField(max_length=50,help_text='Level of education a student is currently in eg Grade 1,PP1.')
    date_created=models.DateField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ClubsOrganization(models.Model):
    # ClubsOrganization represents student clubs or organizations they can join, such as Debate Club, Science Club, etc.
    name = models.CharField(max_length=100)
    date_created=models.DateField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Sport(models.Model):
    # Sport represents the athletic activities a student can participate in, such as Soccer, Basketball, Athletics, etc.
    name = models.CharField(max_length=100)
    date_created=models.DateField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Award(models.Model):
    # Award represents recognitions or honors anyone can receive, such as Best Performer, Most Improved, etc.
    name = models.CharField(max_length=100)
    date_created=models.DateField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

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