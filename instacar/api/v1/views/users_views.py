from rest_framework import permissions, viewsets

from api.v1.serializers.user_serializer import UserProfileSerializer
from users.models import UserProfile


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    http_method_names = ["get", "head", "options"]
    permission_classes = (permissions.IsAdminUser,)
