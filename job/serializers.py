from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Category, Type, Jobs, ApplyJob, Like


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')


class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = ('id', 'title')


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Jobs
        fields = ('id', 'title', 'job_type', 'company', 'location', 'price', 'description', 'author', 'category')


class JobRUDSerializer(serializers.ModelSerializer):
    job_type = TypeSerializer(read_only=True, many=True)
    category = CategorySerializer(required=False)

    class Meta:
        model = Jobs
        fields = ('id', 'title', 'job_type', 'company', 'location', 'price', 'description', 'author', 'category')

        extra_kwargs = {

        }

    # def validate(self, attrs):
    #     request = self.context['request']
    #     author = request.user
    #     print(author.role)
    #     if not author.role == '2':
    #         print(author.role)
    #         raise ValidationError()
    #     return attrs


class ApplyJobSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApplyJob
        fields = ['id', 'job', 'name', 'resume', 'created_date']


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ['id', 'author', 'jobs']
