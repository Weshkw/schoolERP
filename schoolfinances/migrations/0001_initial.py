# Generated by Django 4.2.16 on 2024-11-10 08:20

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('identity', '0001_initial'),
        ('studentmanagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TermOrSemester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the term or semester (e.g., Term 1, Semester 2).', max_length=50)),
                ('start_date', models.DateField(help_text='Start date of the term or semester.')),
                ('end_date', models.DateField(help_text='End date of the term or semester.')),
                ('academic_year', models.CharField(help_text='Academic year in the format YYYY-YYYY (e.g., 2024-2025).', max_length=9)),
                ('school', models.ForeignKey(help_text='Select the school associated with this term or semester.', on_delete=django.db.models.deletion.PROTECT, to='identity.school')),
            ],
        ),
        migrations.CreateModel(
            name='PayableFee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_fees', models.DecimalField(decimal_places=2, help_text='Total amount payable for this term or semester.', max_digits=10)),
                ('due_date', models.DateField(help_text='Final date by which the fees should be paid.')),
                ('description', models.TextField(blank=True, help_text='Brief description of the fees purpose (e.g., Tuition fees, Lab fees).')),
                ('school', models.ForeignKey(help_text='School associated with these fees.', on_delete=django.db.models.deletion.PROTECT, to='identity.school')),
                ('term_or_semester', models.ForeignKey(help_text='Term or semester these fees apply to.', on_delete=django.db.models.deletion.PROTECT, to='schoolfinances.termorsemester')),
            ],
        ),
        migrations.CreateModel(
            name='FeesStructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(help_text='Description of the fees structure (e.g., Annual fee breakdown).')),
                ('file', models.FileField(help_text='Upload a PDF file of the fees structure.', upload_to='fees_structure/')),
                ('upload_date', models.DateField(auto_now_add=True, help_text='Date when the fees structure was uploaded.')),
                ('school', models.ForeignKey(help_text='School associated with these fees structure.', on_delete=django.db.models.deletion.PROTECT, to='identity.school')),
            ],
        ),
        migrations.CreateModel(
            name='FeePayment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('amount_paid', models.DecimalField(decimal_places=2, help_text='Amount the student has paid.', max_digits=10)),
                ('payment_date', models.DateField(help_text='Date the payment was made.')),
                ('payment_method', models.CharField(choices=[('Cash', 'Cash'), ('Bank Deposit', 'Bank Deposit'), ('Bank Transfer', 'Bank Transfer'), ('M-Pesa Payment', 'M-Pesa Payment')], help_text='Method used for the payment (e.g., Cash, Bank Deposit).', max_length=20)),
                ('narration', models.TextField(blank=True, help_text='Optional notes or details about the payment.')),
                ('date_created', models.DateField(auto_now_add=True, help_text='Date when this payment record was created.')),
                ('date_updated', models.DateTimeField(auto_now=True, help_text='Date when this payment record was last updated.')),
                ('expected_fee_this_term', models.ForeignKey(help_text='The fee amount that is expected to be paid for this term.', on_delete=django.db.models.deletion.PROTECT, to='schoolfinances.payablefee')),
                ('student', models.ForeignKey(help_text='Student making the payment.', on_delete=django.db.models.deletion.PROTECT, to='studentmanagement.student')),
                ('term_or_semester', models.ForeignKey(help_text='Term or semester the payment is for.', on_delete=django.db.models.deletion.PROTECT, to='schoolfinances.termorsemester')),
            ],
        ),
    ]