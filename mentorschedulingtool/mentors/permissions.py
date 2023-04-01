
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsSuperUserOrReadOnly(BasePermission):
    """
    Custom permission to only allow superusers to modify objects,
    but allow all users to have read-only access.
    """
    def has_permission(self, request, view):
        # Allow read-only access for all users
        if request.method in SAFE_METHODS:
            return True
        # Only allow superusers to modify objects
        return request.user.is_superuser
    
class IsOwnProfile(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.id == request.user.id