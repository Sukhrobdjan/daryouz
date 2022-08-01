from django.shortcuts import render
from .serializers import LinkSerializer,CategorySerializer,PostSerializer
from rest_framework import permissions
from .models import Post
from rest_framework import generics

class PostView(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]