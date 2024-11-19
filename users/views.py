from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import CustomUserSerializer

class TestUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request) -> Response:
        try:
            user_data = CustomUserSerializer(request.user).data
            return Response({
                'message': 'Вы успешно аутентифицированы!',
                'user': user_data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)