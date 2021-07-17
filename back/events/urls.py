from rest_framework import routers
from django.urls import include, path
from . import views


app_name = 'events'

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'presences', views.PresenceViewSet)
router.register(r'comments', views.CommentViewSet)

urlpatterns = [
    path("user/", views.LoggedUserView.as_view()),
    path("", include(router.urls)),
]