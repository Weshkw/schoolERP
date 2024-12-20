# Generated by Django 4.2.16 on 2024-11-28 20:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('identity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Name of the award (e.g., Best Performer, Most Improved).', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClubsOrganization',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Name of the club or organization (e.g., Debate Club).', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Educational level (e.g., Grade 1, PP1).', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Guardian',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('national_id_number', models.CharField(blank=True, help_text='National ID number of the guardian.', max_length=50, null=True, unique=True)),
                ('guardian_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('school', models.ManyToManyField(help_text='Schools a guardian has a student in.', to='identity.school')),
            ],
            options={
                'verbose_name': 'Guardian',
                'verbose_name_plural': 'Guardians',
            },
        ),
        migrations.CreateModel(
            name='ReportCard',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('grade', models.ForeignKey(help_text='Grade level of the report card.', on_delete=django.db.models.deletion.CASCADE, to='studentmanagement.grade')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Name of the sport (e.g., Soccer, Basketball).', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudentLeadershipTitle',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Name of the title, e.g., Prefect, Game Captain.', max_length=100, unique=True)),
                ('description', models.TextField(blank=True, help_text='Optional description of the title.', null=True)),
            ],
            options={
                'verbose_name': 'Student Leadership Title',
                'verbose_name_plural': 'Student Leadership Titles',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Name of the academic subject (e.g., Math, Science).', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, help_text='This is where one resides, e.g., Nairobi ABC estate.', max_length=100, null=True)),
                ('gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHER', 'Other')], max_length=10)),
                ('nationality', models.CharField(choices=[('KENYAN', 'Kenyan'), ('OTHERS', 'Others')], max_length=100)),
                ('full_name', models.CharField(help_text='For students, provide the full name on the birth certificate.', max_length=100)),
                ('student_identity', models.CharField(help_text='Unique student identifier in the school (e.g., Admission number).', max_length=255)),
                ('enrollment_date', models.DateField(help_text='Date the student was admitted into the school.')),
                ('emergency_contact_name', models.CharField(help_text="Name of the student's emergency contact.", max_length=255)),
                ('emergency_contact_relationship', models.CharField(choices=[('parent or guardian', 'Parent or Guardian'), ('uncle', 'Uncle'), ('aunt', 'Aunt'), ('grandparent', 'Grandparent'), ('cousin', 'Cousin'), ('trusted family friend', 'Trusted Family Friend')], help_text='Relationship between the emergency contact and the student.', max_length=100)),
                ('emergency_contact_phone', phonenumber_field.modelfields.PhoneNumberField(help_text='Phone number of the emergency contact, preferably someone who can respond quickly in emergencies.', max_length=128, region=None)),
                ('awards', models.ManyToManyField(blank=True, help_text='Awards the student has received.', to='studentmanagement.award')),
                ('clubs', models.ManyToManyField(blank=True, help_text='Clubs the student is a member of.', to='studentmanagement.clubsorganization')),
                ('grade', models.ForeignKey(help_text='Current grade level of the student.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='studentmanagement.grade')),
                ('parentguardian', models.ForeignKey(help_text='Parent or guardian associated with the student.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='studentmanagement.guardian')),
                ('school', models.ForeignKey(help_text='School a student attends.', on_delete=django.db.models.deletion.CASCADE, to='identity.school')),
                ('sports', models.ManyToManyField(blank=True, help_text='Sports the student participates in.', to='studentmanagement.sport')),
                ('student_leadership_role', models.ManyToManyField(blank=True, help_text='Name of the title, e.g., Prefect, Game Captain.', to='studentmanagement.studentleadershiptitle')),
                ('subjects', models.ManyToManyField(blank=True, help_text='Subjects the student is taking.', to='studentmanagement.subject')),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
                'unique_together': {('school', 'student_identity')},
            },
        ),
        migrations.CreateModel(
            name='ReportCardSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(help_text='Grade received in the subject.', max_length=10)),
                ('report_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentmanagement.reportcard')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentmanagement.subject')),
            ],
        ),
        migrations.AddField(
            model_name='reportcard',
            name='student',
            field=models.ForeignKey(help_text='Student whose report card is being recorded.', on_delete=django.db.models.deletion.CASCADE, to='studentmanagement.student'),
        ),
        migrations.AddField(
            model_name='reportcard',
            name='subjects',
            field=models.ManyToManyField(help_text='Subjects and their grades in the report card.', through='studentmanagement.ReportCardSubject', to='studentmanagement.subject'),
        ),
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date', models.DateField(help_text='Date of the medical record.')),
                ('description', models.TextField(help_text='Description of the medical condition or treatment.')),
                ('student', models.ForeignKey(help_text='Student whose medical record is being recorded.', on_delete=django.db.models.deletion.CASCADE, to='studentmanagement.student')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HomeworkAssignment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(help_text='Description of the homework assignment.')),
                ('due_date', models.DateField(help_text='Due date for the homework assignment.')),
                ('grade', models.ForeignKey(help_text='Grade level for the homework assignment.', on_delete=django.db.models.deletion.CASCADE, to='studentmanagement.grade')),
                ('subject', models.ForeignKey(help_text='Subject for the homework assignment.', on_delete=django.db.models.deletion.CASCADE, to='studentmanagement.subject')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date', models.DateField(help_text='Date of the attendance record.')),
                ('status', models.CharField(choices=[('present', 'Present'), ('absent', 'Absent'), ('late', 'Late')], help_text='Attendance status.', max_length=50)),
                ('student', models.ForeignKey(help_text='Student whose attendance is being recorded.', on_delete=django.db.models.deletion.CASCADE, to='studentmanagement.student')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
