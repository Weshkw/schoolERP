from django.contrib.auth.models import AbstractUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
import uuid

class TimeStampedModel(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        primary_key=True
    )
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class CustomUserManager(BaseUserManager):
    def create_user(self, username, full_name, email=None, password=None, date_of_birth=None, gender=None, nationality=None):
        if not username:
            raise ValidationError({
                'username': _('Username is required')
            })
        if not password:
            raise ValidationError({
                'password': _('Password is required')
            })

        email = self.normalize_email(email)
        user = self.model(
            username=username,
            full_name=full_name,
            email=email,
            date_of_birth=date_of_birth,
            gender=gender,
            nationality=nationality,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, full_name, email=None, password=None, date_of_birth=None, gender=None, nationality=None):
        user = self.create_user(
            username=username,
            full_name=full_name,
            email=email,
            password=password,
            date_of_birth=date_of_birth,
            gender=gender,
            nationality=nationality,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class School(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True, help_text="Full name of the school.")
    address = models.TextField(help_text="Physical address of the school, e.g., Witeithie in Kiambu county.")
    contact_phonenumber = PhoneNumberField(help_text=_("Primary contact number for the school."))
    contact_email = models.EmailField(unique=True, help_text="Primary email address for the school.")
    established_date = models.DateField(null=True, blank=True, help_text="Date when the school was established.")
    school_type = models.CharField(max_length=50, choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('tertiary', 'Tertiary')], help_text="Type of school.")

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        primary_key=True
    )
    username = models.CharField(
        max_length=150,
        unique=True,
        error_messages={
            'unique': _('This phone number is already registered in the system.'),
        },
    )
    full_name = models.CharField(
        max_length=100,
        help_text='For students, provide the full name on the birth certificate. For an administrator, teacher, staff, or parent, provide the name on the ID card.'
    )
    email = models.EmailField(
        null=True,
        blank=True,
        unique=True,  # unique across system
        help_text='Required for administrators and teachers.',
        error_messages={
            'unique': _('This email address is already registered in the system.')
        }
    )
    phone_number = PhoneNumberField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text='This is where one resides, e.g., Nairobi ABC estate.'
    )

    GENDER_CHOICES = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
        ('OTHER', 'OTHER')
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    NATIONALITY_CHOICES = (
        ('KENYAN', 'KENYAN'),
        ('OTHERS', 'OTHERS'),
    )
    nationality = models.CharField(max_length=100, choices=NATIONALITY_CHOICES)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['full_name', 'date_of_birth', 'gender', 'nationality']

    class Meta:
        verbose_name = "System User"
        verbose_name_plural = "System Users"

    def save(self, *args, **kwargs):
        if not self.password:
            self.set_password(str(self.phone_number))  # Set a default password if none is provided
        super().save(*args, **kwargs)
