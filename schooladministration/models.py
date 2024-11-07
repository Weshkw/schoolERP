from django.db import models
from django.contrib.auth.hashers import make_password
from identity.models import CustomUser, School
from phonenumber_field.modelfields import PhoneNumberField

class AdministratorRank(models.Model):
    title = models.CharField(
        max_length=255,
        help_text="This is the rank an administrator holds, e.g., principal, deputy principal, headteacher, etc."
    )
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Administrator(CustomUser):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    ranks = models.ManyToManyField(
        AdministratorRank, 
        help_text="Administrator's ranks within the school",
        related_name="administrators"
    )
    professional_identity = models.CharField(
    max_length=255,
    null=True,
    blank=True,
    help_text="Professional identifier assigned by an organization, e.g., TSC number for teachers."
    )
    national_id_number = models.CharField(unique=True, max_length=50,null=True,blank=True, )
    phone_number = PhoneNumberField(unique=True,default=None)
    date_of_joining = models.DateField(null=True, blank=True, help_text="Date the administrator joined the school.")
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.username = self.phone_number
        self.password = make_password(f'{self.phone_number}')
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Administrator"
        verbose_name_plural = "Administrators"

    def __str__(self):
        rank_titles = ", ".join(rank.title for rank in self.ranks.all())
        return f"{self.national_id_or_birth_cert_name} - {rank_titles}"
