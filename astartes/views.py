from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import MarineSerializer,PostSerializer
from .models import Marine,Post
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly,IsAuthenticated


class MarineListView(ListCreateAPIView):
    queryset = Marine.objects.all()
    serializer_class = MarineSerializer
    permission_classes= [IsAuthenticated,IsOwnerOrReadOnly]

class MarineDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Marine.objects.all()
    serializer_class = MarineSerializer
    Permission_classes=[IsOwnerOrReadOnly,IsAuthenticated]

class PostListView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    Permission_classes=[IsAuthenticated,IsOwnerOrReadOnly]

class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    Permission_classes=[IsOwnerOrReadOnly,IsAuthenticated]
    
