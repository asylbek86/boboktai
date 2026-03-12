from django.urls import path

from .views import LessonListCreateView, VideoListCreateView

urlpatterns = [
    path("lessons/", LessonListCreateView.as_view(), name="lesson-list-create"),
    path("videos/", VideoListCreateView.as_view(), name="video-list-create"),
]

