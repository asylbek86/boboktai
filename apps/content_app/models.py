from django.db import models


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="videos", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

