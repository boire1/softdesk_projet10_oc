# permissions.py
# from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsProjectAuthor(BasePermission):
    """
    Permission personnalisée pour permettre uniquement à l'auteur du projet de le modifier ou le supprimer.
    """
    def has_object_permission(self, request, _, obj):
        # L'utilisateur qui est l'auteur du projet a le droit de le modifier ou le supprimer
        return obj.author == request.user



class IsContributorOrProjectAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Si l'utilisateur est l'auteur du projet
        if obj.author == request.user:
            return True
        # Si l'utilisateur est un contributeur du projet
        if obj.contributor_set.filter(user=request.user).exists():
            return True
        return False

