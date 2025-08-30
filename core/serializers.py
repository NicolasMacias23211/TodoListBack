from rest_framework import serializers
from .models import tasks , users

class tasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = tasks
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = '__all__'