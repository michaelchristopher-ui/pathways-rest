from django.shortcuts import render
from rest_framework import viewsets
from .serializers import student_serializer
from .models import student
# Create your views here.


class student_viewset(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = student_serializer
