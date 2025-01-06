from rest_framework import viewsets
from .models import User, Project, Task, Invoice
from .serializers import UserSerializer, ProjectSerializer, TaskSerializer, InvoiceSerializer
from rest_framework.permissions import IsAuthenticated
# core/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated]