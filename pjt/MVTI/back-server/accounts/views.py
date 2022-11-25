from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
from rest_framework.decorators import authentication_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.contrib.auth import get_user_model

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import UserDetailSerializer
from movies.serializers import CommentSerializer
from .models import User, Mvti

# Create your views here.
@api_view(['GET'])
def userdetail(request, user_pk):
    if request.method == 'GET':
        User = get_user_model()
        user = get_object_or_404(User, pk=user_pk)
        return Response(serializer.data)

@api_view(['POST'])
def usermvti(request, user_pk, mvti_pk):
    if request.method == 'POST':
        user = get_object_or_404(User, pk=user_pk)
        user.mvti = get_object_or_404(Mvti, pk=mvti_pk)
        user.save()
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)