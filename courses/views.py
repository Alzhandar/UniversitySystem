from rest_framework import viewsets, permissions
from .models import Course, Enrollment
from .serializers import CourseSerializer, EnrollmentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return self.queryset  
        elif user.role == 'teacher':
            return self.queryset.filter(instructor=user) 
        elif user.role == 'student':
            return self.queryset  
        return Course.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        if user.role != 'teacher':
            raise PermissionError("Only teachers can create courses.")
        serializer.save(instructor=user)

    def perform_update(self, serializer):
        user = self.request.user
        course = self.get_object() 
        if user.role != 'teacher' or course.instructor != user:
            raise PermissionError("Only the instructor can update this course.")
        serializer.save()
    
class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return self.queryset  