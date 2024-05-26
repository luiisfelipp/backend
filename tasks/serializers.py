from rest_framework import serializers
from .models import *

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'done', 'created_at')
        read_only_fields = ('id', 'created_at')


class PruebaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prueba
        fields = ('id', 'nombre', 'description', 'seca', 'created_at')
        read_only_fields = ('id', 'created_at')
