from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
from django.db import models
from django.core.exceptions import ValidationError
import uuid

class CustomUserManager(BaseUserManager):
    def create_user(self, username, national_id_or_birth_cert_name, email=None, password=None, date_of_birth=None, gender=None, nationality=None):
        if not username:
            raise ValueError('Username is required')

        user = self.model(
            username=username,
            national_id_or_birth_cert_name=national_id_or_birth_cert_name,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            gender=gender,
            nationality=nationality
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, national_id_or_birth_cert_name, email=None, password=None, date_of_birth=None, gender=None, nationality=None):
        user = self.create_user(
            username=username,
            national_id_or_birth_cert_name=national_id_or_birth_cert_name,
            email=email,
            password=password,
            date_of_birth=date_of_birth,
            gender=gender,
            nationality=nationality
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    national_id_or_birth_cert_name = models.CharField(max_length=100,help_text='For student provide the full name on the birth certificate. For a parent provide the name on th ID card')
    email = models.EmailField(null=True,blank=True,help_text='Optional')
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=100, help_text='This is where one resides eg Nairobi ABC estate.')

    GENDER_CHOICES = (
        ('male', 'MALE'),
        ('female', 'FEMALE'),
        ('other', 'Other')
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    NATIONALITY_CHOICES = (
        ('kenyan', 'KENYAN'),
        ('others', 'OTHERS'),
    )
    nationality = models.CharField(max_length=100, choices=NATIONALITY_CHOICES)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['national_id_or_birth_cert_name', 'date_of_birth', 'gender', 'nationality']

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='custom_users',
        related_query_name='custom_user'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_users',
        related_query_name='custom_user'
    )

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if self.email:
            self.email = self.email.lower()
            if CustomUser.objects.filter(email=self.email).exclude(pk=self.pk).exists():
                raise ValidationError('Email addresses must be unique.')
        else:
            self.email = None
        super(CustomUser, self).save(*args, **kwargs)

    def __str__(self):
        return self.national_id_or_birth_cert_name

    


class School(models.Model):
    school_identity = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        help_text="Unique identifier for the school."
    )
    name = models.CharField(max_length=255, unique=True, help_text="Full name of the school.")
    address = models.TextField(help_text="Physical address of the school eg Witeithie in Kiambu county.")
    contact_number = models.CharField(max_length=20, help_text="Primary contact number for the school.")
    email = models.EmailField(unique=True, help_text="Primary email address for the school.")
    principal_name = models.CharField(max_length=255, help_text="Name of the principal or head of the school.")
    established_date = models.DateField(help_text="Date when the school was established.")
    
    school_type = models.CharField(max_length=50, choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('tertiary', 'Tertiary')], help_text="Type of school.")
    date_created=models.DateField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



# class SuperAdmin(CustomUser):
#     pass

# class Admin(CustomUser):
#     pass
#     # Additional fields for Admins can be added here if required.

# class Teacher(CustomUser):
#     tsc_number = models.CharField(max_length=200,unique=True,blank=True, null=True)
#     curriculum_vitae = models.FileField(upload_to='curriculum vitae/',blank=True, null=True)
#     employment_date = models.DateField()
#     position = models.TextField(help_text='Eg Headmaster,Intern Teacher ,Grade2 Classtaeacher etc.')
#     professional_organizations = models.CharField(max_length=200,blank=True, null=True)
#     models.ManyToManyField('Awards', blank=True,help_text='Awards Earned in school.')
#     # Additional fields for Teachers can be added here if required.






