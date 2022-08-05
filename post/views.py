from django.shortcuts import render
from .serializers import LinkSerializer,CategorySerializer,PostSerializer
from rest_framework import permissions
from .models import Post
from rest_framework import generics

class CategoryView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field ='slug'
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs.get('slug', None):
            queryset = queryset.filter(category__slug=self.kwargs['slug'])

        return queryset

class CategoryNews(CategorySerializer):

    pass