from django.db import models
from django.core.exceptions import ValidationError
from studentmanagement.models import Student, Grade
from identity.models import School, TimeStampedModel
import uuid


class TermOrSemester(TimeStampedModel):
    """
    Represents an academic term or semester.
    """
    school = models.ForeignKey(
        School,
        on_delete=models.PROTECT,
        help_text="The school to which this term or semester belongs."
    )
    name = models.CharField(
        max_length=50,
        help_text="Name of the term or semester (e.g., Term 1, Semester 2)."
    )
    start_date = models.DateField(help_text="The start date of the term or semester.")
    end_date = models.DateField(help_text="The end date of the term or semester.")
    academic_year = models.CharField(
        max_length=9,
        help_text="The academic year in the format YYYY-YYYY (e.g., 2024-2025)."
    )

    def __str__(self):
        return f"{self.name} ({self.start_date:%d %B %Y} to {self.end_date:%d %B %Y})"


class FeeAllocationCategory(models.Model):
    """
    Represents a fee allocation category for a school and a specific term or semester.
    """
    school = models.ForeignKey(
        School,
        on_delete=models.PROTECT,
        help_text="The school to which this fee category belongs."
    )
    category_name = models.CharField(
        max_length=100,
        help_text="The name of the fee category (e.g., Academic Fees, Sports Fees)."
    )
    term_or_semester = models.ForeignKey(
        TermOrSemester,
        on_delete=models.PROTECT,
        help_text="The term or semester associated with this fee category."
    )
    base_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="The base amount to be paid for this fee category (cannot be negative)."
    )
    grades = models.ManyToManyField(
        Grade,
        help_text="Grade levels for which this fee category applies."
    )

    def clean(self):
        if self.base_amount < 0:
            raise ValidationError("The base amount to be paid cannot be negative.")

    def __str__(self):
        return f"{self.category_name} - {self.term_or_semester.name}"


class PaymentCollection(models.Model):
    """
    Represents a payment made by a payer for a specific fee category and student.
    """
    school = models.ForeignKey(
        School,
        on_delete=models.PROTECT,
        help_text="The school to which this payment is made to."
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.PROTECT,
        help_text="The student whose payment is made for."
    )
    payer = models.CharField(
        max_length=50,
        help_text="Entity that made the payment."
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="The total amount of the payment."
    )
    payment_date = models.DateField(
        auto_now_add=True,
        help_text="The date when the payment was received."
    )
    payment_method = models.CharField(
        max_length=40,
        choices=[
            ('Cash', 'Cash'),
            ('M-Pesa Payment', 'M-Pesa Payment'),
            ('Bank Deposit', 'Bank Deposit'),
            ('Bank Transfer', 'Bank Transfer'),
        ],
        help_text="The method of payment."
    )
    receipt_number = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        help_text="A unique receipt identifier."
    )
    recorded_by = models.CharField(
        max_length=50,
        help_text="The staff member who recorded the payment."
    )
    term_or_semester = models.ForeignKey(
        TermOrSemester,
        on_delete=models.PROTECT,
        help_text="The academic term or semester associated with this payment."
    )
    category = models.ForeignKey(
        FeeAllocationCategory,
        on_delete=models.PROTECT,
        help_text="The category of the fee allocation."
    )


    def clean(self):
        if self.amount < 0:
            raise ValidationError("The base amount to be paid cannot be negative.")

    @property
    def balance(self):
        total_payments = PaymentCollection.objects.filter(
            student=self.student,
            category=self.category
        ).aggregate(models.Sum('amount'))['amount__sum'] or 0

        return self.category.base_amount - total_payments

    def generate_receipt(self):
        return (
            f"Payment Receipt\n"
            f"Receipt Number: {self.receipt_number}\n"
            f"Student: {self.student}\n"
            f"Amount: {self.amount}\n"
            f"Date: {self.payment_date}\n"
            f"Payment Method: {self.payment_method}\n"
            f"Term/Semester: {self.term_or_semester}\n"
            f"Category: {self.category.category_name}"
        )

    def __str__(self):
        return f"{self.student} - {self.amount} on {self.payment_date}"


class FeesStructure(TimeStampedModel):
    """
    Represents the fees structure for a school, including a description and a PDF file.
    """
    school = models.ForeignKey(
        School,
        on_delete=models.PROTECT,
        help_text="The school associated with this fees structure."
    )
    description = models.TextField(
        help_text="A description of the fees structure (e.g., Annual fee breakdown)."
    )
    file = models.FileField(
        upload_to='fees_structure/',
        help_text="Upload a PDF file of the fees structure."
    )

    def clean(self):
        super().clean()
        if self.file:
            ext = self.file.name.split('.')[-1].lower()
            if ext != 'pdf':
                raise ValidationError("Only PDF files are allowed. Please convert the file to PDF before uploading.")

    def __str__(self):
        return f"Fees Structure for {self.school.name}"
