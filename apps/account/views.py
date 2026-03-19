from rest_framework.views import APIView
from apps.account.models import User
from apps.account.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

# Show all users (class-based view)
class UserListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# User registration view (class-based view)
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

# User login view (class-based view)
class UserLoginView(APIView):
    def post(self, request):
        user = authenticate(
            username=request.data['username'], 
            password=request.data['password']
        )
        if user:
            token, create = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)