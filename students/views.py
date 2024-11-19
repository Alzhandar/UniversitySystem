from rest_framework import viewsets, permissions
from .models import Student
from .serializers import StudentSerializer
from .permissions import IsAdminOrOwner

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrOwner]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return self.queryset  
        elif user.role == 'student':
            return self.queryset.filter(user=user)  
        return Student.objects.none()  

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)