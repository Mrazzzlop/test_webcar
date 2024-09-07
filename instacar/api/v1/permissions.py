from rest_framework import permissions


class IsAdminOrAuthor(permissions.BasePermission):
    """
    Разрешение редактировать и удалять объекты
    только администраторам и их авторам.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешаем доступ, если пользователь администратор
        if request.user.is_staff:
            return True

        # Проверяем, является ли пользователь автором объекта
        author_field = getattr(obj, 'author', None)
        if author_field is not None:
            return author_field == request.user

        owner_field = getattr(obj, 'owner', None)
        if owner_field is not None:
            return owner_field == request.user

        return False
