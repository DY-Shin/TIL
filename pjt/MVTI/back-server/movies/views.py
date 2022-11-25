
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
from rest_framework.decorators import authentication_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieListSerializer, MovieSerializer, CommentSerializer, MvtiSerializer
from .models import Movie, Comment, Mvti
from random import sample


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def movie_list(request):
    if request.method == 'GET':
        # Movies = Movie.objects.all()
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    # Movie = Movie.objects.get(pk=Movie_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def movie_like(request, movie_pk, user_pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        if movie.like_user.filter(pk=user_pk).exists():
            likes = True
        else:
            likes = False
        like_status = {
            'likes': likes,
        }
        return Response(like_status, status=status.HTTP_200_OK)

# 상세 영화 좋아요(POST)
    if request.method == 'POST':
        movie = get_object_or_404(Movie, pk=movie_pk)
        if movie.like_user.filter(pk=user_pk).exists():
            movie.like_user.remove(request.user)
            liked = False
        else:
            movie.like_user.add(request.user)
            liked = True
        like_status = {
            'liked':liked,
            # 좋아요 여부
            'count':movie.like_user.count(),
            # 좋아요한 사람의 수
        }
        return Response(like_status, status=status.HTTP_200_OK)

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def movie_like(request, movie_pk, user_pk):
# # 상세 영화 좋아요(POST)
#     if request.method == 'POST':
#         movie = get_object_or_404(Movie, pk=movie_pk)
#         if movie.like_user.filter(pk=user_pk).exists():
#             movie.like_user.remove(request.user)
#             liked = False
#         else:
#             movie.like_user.add(request.user)
#             liked = True
#         like_status = {
#             'liked':liked,
#             # 좋아요 여부
#             'count':movie.like_user.count(),
#             # 좋아요한 사람의 수
#         }
#         return Response(like_status, status=status.HTTP_200_OK)

@api_view(['GET'])
def user_like(request, user_pk):
    if request.method == 'GET':
        user = request.user
        like_movies = user.like_movies
        serializer = MovieListSerializer(like_movies, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def user_comments(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    data = []
    comments_pk = request.data
    for comment_pk in comments_pk:
        comment = get_object_or_404(Comment, pk=comment_pk)
        serializer = CommentSerializer(comment)
        data.append(serializer.data)
    return Response(data)

@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        # comments = Comment.objects.all()
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    else:
        if request.user == comment.user:
            if request.method == 'DELETE':
                comment.delete()
                data = {
                    "message": "삭제되었습니다."
                }
                # print('==========================')
                return Response(data, status=status.HTTP_204_NO_CONTENT)

            elif request.method == 'PUT':
                serializer = CommentSerializer(comment, data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


@api_view(['GET', 'POST'])
def comment_create(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    # movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        comments = movie.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def mvti(request, mvti_pk):
    if request.method == 'GET':
        mvti = Mvti.objects.get(pk=mvti_pk)
        serializer = MvtiSerializer(mvti)
        return Response(serializer.data)

@api_view(['GET'])
def recommended(request, mvti_pk):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        # user = request.user
        mvti = Mvti.objects.get(pk=mvti_pk)
        # if request.user.is_authenticated:
        my_genres = [
            mvti.genre1,
            mvti.genre2,
            mvti.genre3,
            mvti.genre4,
            mvti.genre5,
            ]    
        recommendations_list = set()
        for movie in movies:
            genres = movie.genres.all()
            for genre in genres:
                if genre.pk in my_genres:
                    recommendations_list.add(movie)
        recommendations = sample(list(recommendations_list), 20)
        serializer = MovieSerializer(recommendations, many=True)
        return Response(serializer.data)