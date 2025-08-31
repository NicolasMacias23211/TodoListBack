from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import tasks , users
from .serializers import tasksSerializer , UserSerializer

class tasksViewSet(viewsets.ModelViewSet):
    queryset = tasks.objects.all()
    serializer_class = tasksSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = users.objects.all()
    serializer_class = UserSerializer

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = users.objects.get(email=email, password=password)
            serializer = UserSerializer(user)
            return Response({'success': True, 'user': serializer.data})
        except users.DoesNotExist:
            return Response({'success': False, 'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)