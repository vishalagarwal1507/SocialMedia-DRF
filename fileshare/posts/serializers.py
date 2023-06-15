from rest_framework import serializers
from .models import Post, Upvote, Comment

class PostSerializer(serializers.ModelSerializer):

    user= serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Post
        fields = ['id','user','title','body','created','updated','upvote_count']


class UpvoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Upvote
        fields = ['id','user','post']


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id','user','post','body','created']