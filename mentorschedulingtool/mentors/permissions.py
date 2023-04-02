
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
    """
    Provides requested user access only to own profile page
    note: only superusers can edit any user
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_superuser:
            return True
        return obj.id == request.user.id