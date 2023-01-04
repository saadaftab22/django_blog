from django.shortcuts import render
from .models import Category, Blog
from .serializers import CategorySerializer, BlogSerializer
from rest_framework import generics, filters
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS, IsAdminUser
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class OwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.user == request.user


class CategoryPagination(PageNumberPagination):
    page_size = 5


class CategoryList(generics.ListCreateAPIView):
    search_fields = ['name']
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated | ReadOnly]
    authentication_classes = [TokenAuthentication,]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryListPaginated(generics.ListCreateAPIView):
    search_fields = ['name']
    pagination_class = CategoryPagination
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated | ReadOnly]
    authentication_classes = [TokenAuthentication,]
    queryset = Category.objects.order_by()
    serializer_class = CategorySerializer


class CategoryDelete(generics.RetrieveDestroyAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser | ReadOnly]
    authentication_classes = [TokenAuthentication,]

    def get_queryset(self):
        return Category.objects.filter(pk=self.kwargs['pk'])

class BlogPagination(PageNumberPagination):
    page_size = 6


class BlogList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated | ReadOnly]
    authentication_classes = [TokenAuthentication,]
    pagination_class = BlogPagination
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BlogCategoryList(generics.ListAPIView):
    pagination_class = BlogPagination
    serializer_class = BlogSerializer

    def get_queryset(self):
        return Blog.objects.filter(category=self.kwargs['pk'])


class BlogDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer
    permission_classes = [OwnerPermission | ReadOnly]
    authentication_classes = [TokenAuthentication,]

    def get_queryset(self):
        return Blog.objects.filter(pk=self.kwargs['pk'])


class BlogUserList(generics.ListAPIView):
    pagination_class = BlogPagination
    serializer_class = BlogSerializer

    def get_queryset(self):
        return Blog.objects.filter(user=self.kwargs['pk'])
