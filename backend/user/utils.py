from rest_framework.permissions import BasePermission

def user_data(user):
    return {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "username": user.username,
        "email": user.email,
    }
class IsNotAuthenticated(BasePermission):
    """
    Allows access only to non authenticated users.
    """

    def has_permission(self, request, view):
        return not bool(request.user and request.user.is_authenticated)
