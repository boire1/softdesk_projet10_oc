from django.db import models
from user_app.models import CustomUser
# from rest_framework import permissions


class Project(models.Model): 
    name = models.CharField(max_length=100)
    description = models.TextField()
    project_type = models.CharField(max_length=20)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering=['-created_time']
        


# class IsProjectAuthor(permissions.BasePermission):
#     """
#     Permission personnalisée pour permettre uniquement à l'auteur du projet de le modifier ou le supprimer.
#     """

#     def has_object_permission(self, request, _, obj):
#         # L'utilisateur qui est l'auteur du projet a le droit de le modifier ou le supprimer
#         return obj.author == request.user
        
        
class Contributor(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
       return str(self.user.username)
    
    class Meta:
        ordering=['-created_time'] 
        
# class IsContributorOrProjectAuthor(permissions.BasePermission):
#     """
#     Permission personnalisée pour permettre uniquement à l'utilisateur associé au contributeur ou à l'auteur du projet associé de modifier ou supprimer le contributeur.
#     """

#     def has_object_permission(self, request, _, obj):
#         # L'utilisateur associé au contributeur ou l'auteur du projet associé a le droit de le modifier ou le supprimer
#         return obj.user == request.user or obj.project.author == request.user
               
