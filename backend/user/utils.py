from rest_framework.permissions import BasePermission

class IsNotAuthenticated(BasePermission):
    """
    Allows access only to non authenticated users.
    """

    def has_permission(self, request, view):
        return not bool(request.user and request.user.is_authenticated)
