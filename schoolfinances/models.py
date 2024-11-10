from django.db import models
from django.core.exceptions import ValidationError
from studentmanagement.models import Student
from identity.models import School
import uuid


class TermOrSemester(models.Model):
    school = models.ForeignKey(School, on_delete=models.PROTECT, help_text="Select the school associated with this term or semester.")
    name = models.CharField(max_length=50, help_text="Name of the term or semester (e.g., Term 1, Semester 2).")
    start_date = models.DateField(help_text="Start date of the term or semester.")
    end_date = models.DateField(help_text="End date of the term or semester.")
    academic_year = models.CharField(max_length=9, help_text="Academic year in the format YYYY-YYYY (e.g., 2024-2025).")

    def __str__(self):
        formatted_start_date = self.start_date.strftime('%d %B %Y')
        formatted_end_date = self.end_date.strftime('%d %B %Y')
        return f"{self.name} ({formatted_start_date} to {formatted_end_date})"


class PayableFee(models.Model):
    school = models.ForeignKey(School, on_delete=models.PROTECT, help_text="School associated with these fees.")
    term_or_semester = models.ForeignKey(TermOrSemester, on_delete=models.PROTECT, help_text="Term or semester these fees apply to.")
    total_fees = models.DecimalField(max_digits=10, decimal_places=2, help_text="Total amount payable for this term or semester.")
    due_date = models.DateField(help_text="Final date by which the fees should be paid.")
    description = models.TextField(blank=True, help_text="Brief description of the fees purpose (e.g., Tuition fees, Lab fees).")

    def __str__(self):
        return f"{self.school} - {self.term_or_semester} - {self.total_fees}"


class FeePayment(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    student = models.ForeignKey(Student, on_delete=models.PROTECT, help_text="Student making the payment.")
    term_or_semester = models.ForeignKey(TermOrSemester, on_delete=models.PROTECT, help_text="Term or semester the payment is for.")
    expected_fee_this_term = models.ForeignKey(PayableFee, on_delete=models.PROTECT, help_text="The fee amount that is expected to be paid for this term.")
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, help_text="Amount the student has paid.")
    payment_date = models.DateField(help_text="Date the payment was made.")
    payment_method = models.CharField(
        max_length=20,
        choices=[
            ('Cash', 'Cash'),
            ('Bank Deposit', 'Bank Deposit'),
            ('Bank Transfer', 'Bank Transfer'),
            ('M-Pesa Payment', 'M-Pesa Payment'),
        ],
        help_text="Method used for the payment (e.g., Cash, Bank Deposit)."
    )
    narration = models.TextField(blank=True, help_text="Optional notes or details about the payment.")
    date_created = models.DateField(auto_now_add=True, help_text="Date when this payment record was created.")
    date_updated = models.DateTimeField(auto_now=True, help_text="Date when this payment record was last updated.")

    def __str__(self):
        return f"{self.student} - {self.amount_paid} on {self.payment_date}"


class FeesStructure(models.Model):
    school = models.ForeignKey(School, on_delete=models.PROTECT, help_text="School associated with these fees structure.")
    description = models.TextField(help_text="Description of the fees structure (e.g., Annual fee breakdown).")
    file = models.FileField(upload_to='fees_structure/', help_text="Upload a PDF file of the fees structure.")
    upload_date = models.DateField(auto_now_add=True, help_text="Date when the fees structure was uploaded.")

    def clean(self):
        super().clean()
        if self.file:
            ext = self.file.name.split('.')[-1].lower()
            if ext != 'pdf':
                raise ValidationError("Only PDF files are allowed. Please convert the file to PDF before uploading.")

    def __str__(self):
        return f'FEES STRUCTURE FOR{self.school.name}'
