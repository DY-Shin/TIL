from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
# from rest_framework.fields import SerializerMethodField
from movies.models import Comment, Mvti
from .models import User

class CustomRegisterSerializer(RegisterSerializer):
    class Meta:
        model = User
        read_only_fields = ('mvti',)
    # level = serializers.CharField(max_length=100)

    # def get_cleaned_data(self):
    #     data = super().get_cleaned_data()
    #     data['level'] = self.validated_data.get('level','')
    #     return data

class UserDetailSerializer(serializers.ModelSerializer):

    class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('pk', 'content', 'user', 'created_at', 'updated_at', 'movie', 'score', 'content', 'updated_at',)
            read_only_fields = ('movie', 'user')

    comment_set = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('pk', 'username', 'comment_set', 'mvti',)
    # class MovieSerializer(serializers.ModelSerializer):

    #     class Meta:
    #         model = Movie
    #         fields = ('pk', 'title',)

    # movie = MovieSerializer(read_only=True)

    class MvtiSerializer(serializers.ModelSerializer):
        class Meta:
            model = Mvti
            fields = ('pk', 'name', 'genre1', 'genre2', 'genre3',)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'mvti')
        read_only_fields = ('mvti',)
        
    
    