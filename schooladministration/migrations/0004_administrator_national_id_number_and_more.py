# Generated by Django 4.2.16 on 2024-11-06 18:54

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('schooladministration', '0003_administrator_professional_identity'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrator',
            name='national_id_number',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='administrator',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default=None, max_length=128, region=None, unique=True),
        ),
        migrations.AlterField(
            model_name='administrator',
            name='date_of_joining',
            field=models.DateField(blank=True, help_text='Date the administrator joined the school.', null=True),
        ),
    ]