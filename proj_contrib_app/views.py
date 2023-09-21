from rest_framework import viewsets, permissions
from .models import Project, Contributor
from .serializers import ProjectSerializer, ContributorSerializer
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .permissions import IsProjectAuthor
from .permissions import IsContributorOrProjectAuthor


class ContributorViewSet(viewsets.ModelViewSet):
    queryset = Contributor.objects.all()
    #  créer un serializer pour Contributor
    serializer_class = ContributorSerializer  
    permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.IsAuthenticated, IsContributorOrProjectAuthor]


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-created_time')
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.IsAuthenticated, IsProjectAuthor]
    
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=self.request.user)      
        
        # Créer un contributeur pour le projet avec l'utilisateur courant
        Contributor.objects.create(user=request.user, project=serializer.instance)
      
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
    # Ne permet pas de changer l'auteur
        if 'author' in request.data:
            del request.data['author']
        
        return super(ProjectViewSet, self).update(request, *args, **kwargs)

