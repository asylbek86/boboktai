from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("apps.auth_app.urls")),
    path("api/users/", include("apps.users.urls")),
    path("api/", include("apps.content_app.urls")),
]

