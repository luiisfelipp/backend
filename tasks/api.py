from rest_framework import viewsets, permissions
from .models import *
from .serializers import TaskSerializer
from .serializers import PruebaSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permision_classes =[permissions.AllowAny]
    serializer_class = TaskSerializer

class PruebaViewSet(viewsets.ModelViewSet):
    queryset = Prueba.objects.all()
    permision_classes =[permissions.AllowAny]
    serializer_class = PruebaSerializer