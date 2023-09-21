from django.db import models
from user_app.models import CustomUser
from proj_contrib_app.models import Project,Contributor
from uuid import uuid4
    
class Issue(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length=20, default='To Do')
    priority = models.CharField(max_length=10)
    tag = models.CharField(max_length=10)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigned_contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ]
    TAG_CHOICES = [
        ('BUG', 'Bug'),
        ('FEATURE', 'Feature'),
        ('TASK', 'Task'),
    ]
    STATUS_CHOICES = [
        ('TO DO', 'To Do'),
        ('IN PROGRESS', 'In Progress'),
        ('FINISHED', 'Finished'),
    ]
    
    # ... other fields ...
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    tag = models.CharField(max_length=10, choices=TAG_CHOICES)
    status = models.CharField(max_length=20, default='TO DO', choices=STATUS_CHOICES)
    # ...
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['-created_time']


class Comment(models.Model):
    text = models.TextField()
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering=['-created_time']  