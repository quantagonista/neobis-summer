from django.shortcuts import render
from rest_framework import generics

from system.models import Course
from system.serializers import CourseSerializer


class CoursesListView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CoursesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
