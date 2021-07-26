from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
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

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.owner == request.user

class IsUserOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.user == request.user

class LoggedUserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

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
    permission_classes = [IsUserOrReadOnly]

class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows events to be viewed or edited.
    """
    queryset = Event.objects.all().order_by('-created')
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly]

    @action(methods=['get'], detail=True)
    def comments(self, request, pk=None):
        try:
            event = Event.objects.get(id=pk)
        except Event.DoesNotExist:
            return Response({"info": "Event not found."},
                            status=status.HTTP_400_BAD_REQUEST)
        comments = event.comment_set.all()
        return Response(CommentSerializer(comments, many=True).data)

class PresenceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows presences to be viewed or edited.
    """
    queryset = Presence.objects.all()
    serializer_class = PresenceSerializer
    permission_classes = [IsUserOrReadOnly]

class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comments to be viewed or edited.
    """
    queryset = Comment.objects.all().order_by('-created')
    serializer_class = CommentSerializer
    permission_classes = [IsUserOrReadOnly]

