from rest_framework import serializers
from .models import Blog, Comment, Body
from account.serializers import MyAccountSerializer


class MiniBodySerializer(serializers.ModelSerializer):

    class Meta:
        model = Body
        fields = ('id', 'body', 'post', 'image')


class BlogListCreateSerializer(serializers.ModelSerializer):
    blog_body = MiniBodySerializer(required=False, many=True)

    class Meta:
        model = Blog
        fields = ['id', 'author', 'title', 'image', 'category', 'tags', 'blog_body', 'description', 'created_date']

        extra_kwargs = {
            "author": {'read_only': True},
            "image": {'required': False},
        }


class BlogRUDSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ['id', 'author', 'title', 'image', 'category', 'tags', 'description', 'created_date']

        extra_kwargs = {
            'image': {'required': False},
        }


class MiniCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author', 'blog', 'message', 'top_level_comment_id', 'created_date')


class CommentSerializer(serializers.ModelSerializer):
    author = MyAccountSerializer(read_only=True)
    children = serializers.SerializerMethodField(read_only=True)

    def get_children(self, obj):
        children = Comment.objects.filter(parent_comment_id=obj.id)
        serializer = MiniCommentSerializer(children, many=True)
        return serializer.data

    class Meta:
        model = Comment
        fields = ('id', 'author', 'blog', 'parent_comment', 'message', 'top_level_comment_id',
                  'children', 'created_date')
        extra_kwargs = {
            'author': {"read_only": True},
            'top_level_comment_id': {"read_only": True},
            'blog': {"read_only": True},
        }

    def create(self, validated_data):
        request = self.context['request']
        blog_id = self.context['blog_id']
        author_id = request.user.id
        instance = Comment.objects.create(author_id=author_id, blog_id=blog_id, **validated_data)
        return instance

