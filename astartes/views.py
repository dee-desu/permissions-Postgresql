from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import MarineSerializer,PostSerializer
from .models import Marine,Post
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly


class MarineListView(ListCreateAPIView):
    queryset = Marine.objects.all()
    serializer_class = MarineSerializer

class MarineDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Marine.objects.all()
    serializer_class = MarineSerializer
    Permission_classes=[IsOwnerOrReadOnly]

class PostListView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    Permission_classes=[AllowAny]

class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    Permission_classes=[IsAuthenticatedOrReadOnly]