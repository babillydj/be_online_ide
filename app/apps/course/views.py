from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Course as CourseDB
from .serializers import CourseDetailSerializer, CourseListSerializer


class CourseList(generics.ListCreateAPIView):
    queryset = CourseDB.objects.all()
    permission_classes = [AllowAny, ]
    serializer_class = CourseListSerializer


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseDB.objects.all()
    permission_classes = [AllowAny, ]
    serializer_class = CourseDetailSerializer
