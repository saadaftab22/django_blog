from rest_framework import serializers
from .models import Category, Blog
from users.serializers import UserSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['pk','name']


class BlogSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    # user = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Blog
        fields = ['pk','title', 'body', 'user', 'category']
        read_only_fields = ('user',)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = UserSerializer(instance.user).data
        response['category'] = CategorySerializer(instance.category, many=True).data
        return response

    # def create(self, request, **kwargs):
    #     serializer = BlogSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(user=request.user)


    # def create(self, validated_data):
    #     category_data = validated_data.pop('category')
    #     blog = Blog.objects.create(**validated_data)
    #     Category.objects.create(blog=blog, **category_data)
    #     return blog