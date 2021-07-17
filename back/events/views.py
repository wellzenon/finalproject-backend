from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, viewsets
from back.accounts.models import CustomUser as User
from back.events.models import (
    Event,
    Presence,
    Comment
)
from .serializers import (
    UserSerializer, 
    EventSerializer, 
    PresenceSerializer, 
    CommentSerializer
)

class LoggedUserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=self.request.user.id)
        return obj

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows events to be viewed or edited.
    """
    queryset = Event.objects.all().order_by('-created')
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]

class PresenceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows presences to be viewed or edited.
    """
    queryset = Presence.objects.all()
    serializer_class = PresenceSerializer
    permission_classes = [permissions.AllowAny]

class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comments to be viewed or edited.
    """
    queryset = Comment.objects.all().order_by('-created')
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]

