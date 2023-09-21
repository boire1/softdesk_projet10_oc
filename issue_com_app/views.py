from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .serializers import IssueSerializers, CommentSerializer
from .models import Issue, Comment
from proj_contrib_app.models import Contributor, Project
from django.db.models import Q
from softdesk.permissions import IsIssueAuthorOrAdmin




class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueSerializers
    permission_classes = [permissions.IsAuthenticated, IsIssueAuthorOrAdmin]
    
    def get_queryset(self):
        user = self.request.user
        # Récupère les issues où l'utilisateur est soit un contributeur du projet, soit le contributeur assigné
        return Issue.objects.filter(Q(project__contributor__user=user) | Q(assigned_contributor__user=user))


    def create(self, request, *args, **kwargs):
        project = Project.objects.get(pk=request.data['project'])

        # Si l'utilisateur n'est pas déjà un contributeur, ajoutez-le comme contributeur.
        if not project.contributor_set.filter(user=request.user).exists():
            Contributor.objects.create(user=request.user, project=project)

        # Créez une copie mutable de request.data
        data = request.data.copy()

        # Mettez à jour 'author' avec l'ID de l'utilisateur connecté
        data['author'] = request.user.id

        # Utilisez cette copie modifiée pour le serializer
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        # Enregistrez l'objet avec l'author mis à jour
        issue = serializer.save(author=request.user)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

def perform_create(self, serializer):
    serializer.save(author=self.request.user)




class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Seuls les contributeurs du projet associé à l'issue peuvent voir les commentaires
        user = self.request.user
        return Comment.objects.filter(issue__project__contributor__user=user)

    def create(self, request, *args, **kwargs):
        issue = Issue.objects.get(pk=request.data['issue'])
        
        # Vérifiez si l'utilisateur est soit l'auteur de l'issue,
        # soit le contributeur du projet associé à l'issue,
        # soit l'utilisateur assigné à cette issue
        if not (issue.author == request.user or issue.project.contributor_set.filter(user=request.user).exists() or issue.assigned_contributor.user == request.user):
            return Response({"detail": "Vous n'avez pas le droit de commenter cette issue."}, status=status.HTTP_403_FORBIDDEN)

        # Ajoutez manuellement l'auteur du commentaire
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
