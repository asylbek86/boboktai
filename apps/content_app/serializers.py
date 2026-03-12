from rest_framework import serializers

from .models import Lesson, Video


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ["id", "title", "description", "created_at"]
        read_only_fields = ["id", "created_at"]


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ["id", "title", "url", "lesson", "created_at"]
        read_only_fields = ["id", "created_at"]

