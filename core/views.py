from django.shortcuts import render
from rest_framework import viewsets
from .models import tasks , users
from .serializers import tasksSerializer , UserSerializer

class tasksViewSet(viewsets.ModelViewSet):
    queryset = tasks.objects.all()
    serializer_class = tasksSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = users.objects.all()
    serializer_class = UserSerializer
