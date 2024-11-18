from rest_framework import viewsets, permissions
from .models import Course
from .serializers import CourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.role == 'teacher' or self.request.user.role == 'admin':
            serializer.save(instructor=self.request.user)
        else:
            raise PermissionError("Только преподаватели или администраторы могут создавать курсы.")

    def get_queryset(self):
        if self.request.user.role == 'student':
            return self.queryset
        if self.request.user.role == 'teacher':
            return self.queryset.filter(instructor=self.request.user)
        return self.queryset