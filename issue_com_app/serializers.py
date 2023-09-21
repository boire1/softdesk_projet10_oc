from rest_framework import serializers
from issue_com_app.models import Comment , Issue


class IssueSerializers(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    author_name = serializers.SerializerMethodField()
    project_name = serializers.SerializerMethodField()
    assigned_contributor_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Issue    
        fields = ['name', 'project_name', 'description', 'status', 'priority', 'tag', 'project', 
                  'assigned_contributor_name', 'author_name', 'assigned_contributor', 'created_time', 'author']
    def get_author_name(self, obj):
        return obj.author.username

    def get_project_name(self, obj):
        return obj.project.name

    def get_assigned_contributor_name(self, obj):
        return obj.assigned_contributor.user.username


class CommentSerializer(serializers.ModelSerializer):
    issue_name = serializers.SerializerMethodField()
    author_name = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['text', 'issue', 'uuid', 'created_time', 'issue_name', 'author_name']


    def get_issue_name(self, obj):
        return str(obj.issue)

    def get_author_name(self, obj):
        return obj.author.username

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Remove issue and author IDs
        representation.pop('issue', None)
        representation.pop('author', None)
        return representation
    