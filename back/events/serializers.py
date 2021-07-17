from rest_framework import serializers
from back.accounts.models import CustomUser as User
from back.events.models import Event, Presence, Comment


class PresenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presence
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    event_presences = PresenceSerializer(source="presence_set", many=True, read_only=True)
    
    class Meta:
        model = User
        fields = (
            "id",
            "slug",
            "username",
            "first_name",
            "last_name",
            "email",
            "birthday",
            "bio",
            "event_presences",
            "event_comments"
        )
        extra_kwargs = {'password': {'write_only': True}}
        depth = 1

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
    