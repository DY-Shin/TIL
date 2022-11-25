from rest_framework import serializers
from .models import Movie, Comment, Mvti
from django.contrib.auth import get_user_model


class MovieListSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'overview', 'poster_path')
        # fields = ('id', 'title', 'overview', 'user', 'username')


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    moviename =  serializers.CharField(source='movie.title', read_only=True)
    
    class Meta:
        model = Comment
        fields = ('pk', 'username', 'movie', 'content', 'score', 'moviename')
        read_only_fields = ('movie', 'username', 'user', 'moviename')
        # extra_kwargs = {'user': {'required': False}}

    


class MovieSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('user',)


# class CommentListSerializer(serializers.ModelSerializer):
#     class UserSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = get_user_model()
#             fields = ('pk', 'username')
    
#     user = UserSerializer(read_only=True)

#     class Meta:
#         model = Comment
#         fields = ('pk', 'content', 'user', 'created_at', 'updated_at', 'movie', 'score')

class MvtiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mvti
        fields = '__all__'
