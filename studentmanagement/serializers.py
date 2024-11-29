from rest_framework import serializers
from .models import Student,Guardian
from identity.models import CustomUser,School
from studentmanagement.models import Grade, Subject, ClubsOrganization, Sport, Award 
from django.db import transaction
from django.core.exceptions import ValidationError

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class GuardianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guardian
        fields = '__all__'