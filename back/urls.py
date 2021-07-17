from django.contrib import admin
from rest_framework import routers
from django.urls import include, path
from .accounts import urls as authUrls
from .events import urls as eventUrls


urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include(authUrls, namespace="accounts")),
    path("", include(eventUrls, namespace="events")),
]
