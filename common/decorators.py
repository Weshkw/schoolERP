# from functools import wraps
# from django.http import HttpResponseForbidden
# from django.shortcuts import get_object_or_404
# from schooladministration.models import Staff, TeachingStaff, NonTeachingStaff
# from studentmanagement.models import Student, Guardian
# from identity.models import School

# # Decorator to check if the user is any Staff member
# def staff_required(view_func):
#     @wraps(view_func)
#     def _wrapped_view(request, *args, **kwargs):
#         if Staff.objects.filter(user=request.user).exists():
#             return view_func(request, *args, **kwargs)
#         return HttpResponseForbidden("Access denied: You must be a staff member to access this page.")
#     return _wrapped_view

# # Decorator to check if the user is a TeachingStaff member
# def teaching_staff_required(view_func):
#     @wraps(view_func)
#     def _wrapped_view(request, *args, **kwargs):
#         if TeachingStaff.objects.filter(user=request.user).exists():
#             return view_func(request, *args, **kwargs)
#         return HttpResponseForbidden("Access denied: You must be a teaching staff member to access this page.")
#     return _wrapped_view

# # Decorator to check if the user is a NonTeachingStaff member
# def non_teaching_staff_required(view_func):
#     @wraps(view_func)
#     def _wrapped_view(request, *args, **kwargs):
#         if NonTeachingStaff.objects.filter(user=request.user).exists():
#             return view_func(request, *args, **kwargs)
#         return HttpResponseForbidden("Access denied: You must be a non-teaching staff member to access this page.")
#     return _wrapped_view

# # Decorator to check if the user is a Guardian
# def guardian_required(view_func):
#     @wraps(view_func)
#     def _wrapped_view(request, *args, **kwargs):
#         if Guardian.objects.filter(user=request.user).exists():
#             return view_func(request, *args, **kwargs)
#         return HttpResponseForbidden("Access denied: You must be a guardian to access this page.")
#     return _wrapped_view

# # Decorator to check if the user is a Student
# def student_required(view_func):
#     @wraps(view_func)
#     def _wrapped_view(request, *args, **kwargs):
#         if Student.objects.filter(user=request.user).exists():
#             return view_func(request, *args, **kwargs)
#         return HttpResponseForbidden("Access denied: You must be a student to access this page.")
#     return _wrapped_view

# # Decorator to ensure user belongs to a specific school
# def school_specific_access(school_field_name):
#     def decorator(view_func):
#         @wraps(view_func)
#         def _wrapped_view(request, *args, **kwargs):
#             school_id = kwargs.get(school_field_name)
#             school = get_object_or_404(School, id=school_id)

#             # Check if user belongs to the school
#             if Staff.objects.filter(user=request.user, school=school).exists():
#                 return view_func(request, *args, **kwargs)
#             elif Guardian.objects.filter(user=request.user, school=school).exists():
#                 return view_func(request, *args, **kwargs)
#             elif Student.objects.filter(user=request.user, school=school).exists():
#                 return view_func(request, *args, **kwargs)

#             return HttpResponseForbidden("Access denied: You do not belong to this school.")
#         return _wrapped_view
#     return decorator
