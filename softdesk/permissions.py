from rest_framework import permissions

class IsIssueAuthorOrAdmin(permissions.BasePermission):
    """
    Permission personnalisée pour permettre uniquement au créateur de l'Issue ou à un administrateur de modifier l'Issue.
    """

    def has_object_permission(self, request, _, obj):
        # Autoriser toutes les lectures (GET, HEAD ou OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # L'utilisateur assigné à l'Issue a le droit de le modifier
        if obj.assigned_contributor.user == request.user:
            return True

        # Les administrateurs ont toujours le droit de modifier
        return request.user.is_staff
