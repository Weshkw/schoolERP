from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
# from django.db import transaction
# from .serializers import CustomUserSerializer
# from schooladministration.serializers import StaffSerializer, TeachingStaffSerializer, NonTeachingStaffSerializer
# from studentmanagement.serializers import StudentSerializer, GuardianSerializer

def home(request):
    return render(request, 'home.html')  


# class RegistrationViewSet(ViewSet):
#     #issues 1. no atomicity . a user has been created yet staff had an issue 2. username and password should be phone_number and phone number respectively for a staff but that doesnt happen 3. Phone number and email should be unique globally since its used by guardians and staff for authentication 4. for students they dont need system authentication, they only need to provide their school,first name and index number to get resouces ment for them

#     @transaction.atomic
#     def register_staff(self, request):
#         try:
#             user_data = request.data.pop('user')
#             user_serializer = CustomUserSerializer(data=user_data)
#             if user_serializer.is_valid():
#                 user = user_serializer.save()
#                 staff_data = request.data
#                 staff_data['staff_user'] = user.id
#                 staff_serializer = StaffSerializer(data=staff_data)
#                 if staff_serializer.is_valid():
#                     staff_serializer.save()
#                     return Response(staff_serializer.data, status=status.HTTP_201_CREATED)
#                 else:
#                     return Response(staff_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#             else:
#                 return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

#     @transaction.atomic
#     def register_teaching_staff(self, request):
#         try:
#             user_data = request.data.pop('user')
#             user_serializer = CustomUserSerializer(data=user_data)
#             if user_serializer.is_valid():
#                 user = user_serializer.save()
#                 teaching_staff_data = request.data
#                 teaching_staff_data['staff_user'] = user.id
#                 teaching_staff_serializer = TeachingStaffSerializer(data=teaching_staff_data)
#                 if teaching_staff_serializer.is_valid():
#                     teaching_staff_serializer.save()
#                     return Response(teaching_staff_serializer.data, status=status.HTTP_201_CREATED)
#                 else:
#                     return Response(teaching_staff_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#             else:
#                 return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

#     @transaction.atomic
#     def register_non_teaching_staff(self, request):
#         try:
#             user_data = request.data.pop('user')
#             user_serializer = CustomUserSerializer(data=user_data)
#             if user_serializer.is_valid():
#                 user = user_serializer.save()
#                 non_teaching_staff_data = request.data
#                 non_teaching_staff_data['staff_user'] = user.id
#                 non_teaching_staff_serializer = NonTeachingStaffSerializer(data=non_teaching_staff_data)
#                 if non_teaching_staff_serializer.is_valid():
#                     non_teaching_staff_serializer.save()
#                     return Response(non_teaching_staff_serializer.data, status=status.HTTP_201_CREATED)
#                 else:
#                     return Response(non_teaching_staff_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#             else:
#                 return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

#     @transaction.atomic
#     def register_student(self, request):
#         try:
#             user_data = request.data.pop('user')
#             user_serializer = CustomUserSerializer(data=user_data)
#             if user_serializer.is_valid():
#                 user = user_serializer.save()
#                 student_data = request.data
#                 student_data['student_user'] = user.id
#                 student_serializer = StudentSerializer(data=student_data)
#                 if student_serializer.is_valid():
#                     student_serializer.save()
#                     return Response(student_serializer.data, status=status.HTTP_201_CREATED)
#                 else:
#                     return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#             else:
#                 return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

#     @transaction.atomic
#     def register_guardian(self, request):
#         try:
#             user_data = request.data.pop('user')
#             user_serializer = CustomUserSerializer(data=user_data)
#             if user_serializer.is_valid():
#                 user = user_serializer.save()
#                 guardian_data = request.data
#                 guardian_data['guardian_user'] = user.id
#                 guardian_serializer = GuardianSerializer(data=guardian_data)
#                 if guardian_serializer.is_valid():
#                     guardian_serializer.save()
#                     return Response(guardian_serializer.data, status=status.HTTP_201_CREATED)
#                 else:
#                     return Response(guardian_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#             else:
#                 return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)