from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, TeacherViewSet, ClassViewSet, AttendanceViewSet, GradeViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'classes', ClassViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'grades', GradeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
]
