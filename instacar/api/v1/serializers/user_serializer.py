from djoser.serializers import UserSerializer

from users.models import UserProfile


class UserProfileSerializer(UserSerializer):
    """Сериализатор пользователей."""

    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'email')
