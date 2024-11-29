from django.urls import path
# from .views import RegistrationViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('register/staff/', RegistrationViewSet.as_view({'post': 'register_staff'}), name='register-staff'),
    # path('register/teaching-staff/', RegistrationViewSet.as_view({'post': 'register_teaching_staff'}), name='register-teaching-staff'),
    # path('register/non-teaching-staff/', RegistrationViewSet.as_view({'post': 'register_non_teaching_staff'}), name='register-non-teaching-staff'),
    # path('register/student/', RegistrationViewSet.as_view({'post': 'register_student'}), name='register-student'),
    # path('register/guardian/', RegistrationViewSet.as_view({'post': 'register_guardian'}), name='register-guardian'),
]
