from rest_framework import generics, permissions

from .models import Lesson, Video
from .serializers import LessonSerializer, VideoSerializer


class LessonListCreateView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all().order_by("id")
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]


class VideoListCreateView(generics.ListCreateAPIView):
    queryset = Video.objects.all().order_by("id")
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticated]

