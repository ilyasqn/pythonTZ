from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Разрешает редактирование только владельцу объекта.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
