from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework import permissions


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return bool(request.user and (request.user.role == 2))


class IsAdmin(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user and (request.user.role == 2))


class IsOwnUserOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # return obj.id == request.user.id
        return bool(request.user and (request.user.role == 2))
