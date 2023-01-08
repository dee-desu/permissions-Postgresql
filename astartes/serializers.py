from .models import Marine,Post
from rest_framework import serializers

class MarineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marine
        # fields = '__all__'
        fields = ['id','title','region','description']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        # fields = ['id','title','description']