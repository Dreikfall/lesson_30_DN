from rest_framework.permissions import BasePermission

from users.models import UserRole


class OwnerPermission(BasePermission):
    message = 'you not owner or admin/moderator'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner or request.user.role in \
                [UserRole.choices[1][0], UserRole.choices[2][0]]:
            return True
        return False