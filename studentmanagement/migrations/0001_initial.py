# Generated by Django 4.2.16 on 2024-11-04 18:26

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('identity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClubsOrganization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Level of education a student is currently in eg Grade 1,PP1.', max_length=50)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Guardian',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='identity.customuser')),
                ('national_id_number', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(help_text="A parent's phone number helps match them with the right student, even if two parents have similar names. No two parents can have the same phone numbers.", max_length=128, region=None, unique=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Guardian',
                'verbose_name_plural': 'Guardians',
            },
            bases=('identity.customuser',),
        ),
        migrations.CreateModel(
            name='HomeworkAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ReportCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='identity.customuser')),
                ('student_identity', models.CharField(help_text='Eg Admission number of a student or any other unique identity of a student in the school.', max_length=255)),
                ('enrollment_date', models.DateField(help_text='This is the date the student was admitted into the school.')),
                ('emergency_contact_name', models.CharField(max_length=255)),
                ('emergency_contact_relationship', models.CharField(choices=[('parent or guardian', 'PARENT OR GUARDIAN'), ('uncle', 'UNCLE'), ('aunt', 'AUNT'), ('grandparent', 'GRANDPARENT'), ('cousin', 'COUSIN'), ('trusted family friend', 'TRUSTED FAMILY FRIEND')], max_length=100)),
                ('emergency_contact_phone', phonenumber_field.modelfields.PhoneNumberField(help_text='The emergency contact should be someone who is easily reachable by phone and has a close relationship with the student so they can respond quickly during emergencies. ', max_length=128, region=None)),
                ('date_added_to_system', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('awards', models.ManyToManyField(blank=True, to='studentmanagement.award')),
                ('clubs', models.ManyToManyField(blank=True, to='studentmanagement.clubsorganization')),
                ('grade', models.ForeignKey(help_text='Level of education a student is currently in.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='studentmanagement.grade')),
                ('parentguardian', models.ForeignKey(help_text='Can be parent or guardian.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='studentmanagement.guardian')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='identity.school')),
                ('sports', models.ManyToManyField(blank=True, to='studentmanagement.sport')),
                ('subjects', models.ManyToManyField(blank=True, to='studentmanagement.subject')),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
            bases=('identity.customuser',),
        ),
    ]
