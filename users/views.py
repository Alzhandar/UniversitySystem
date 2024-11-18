from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class TestUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            'message': 'Вы успешно аутентифицированы!',
            'user': {
                'username': request.user.username,
                'email': request.user.email,
                'role': request.user.role,
            }
        })