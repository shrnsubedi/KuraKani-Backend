from django.shortcuts import render
from rest_framework import generics, authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .permissions import IsAuthorOrReadOnly
from .models import Post
from .serializers import PostSerializer
from django.http import HttpResponse
# Create your views here.


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class GetUser(APIView):
    authentication_class = [authentication.TokenAuthentication]

    def get(self, request, format=None):
        token = (request.query_params.get("token"))
        user = Token.objects.get(key=token).user
        return Response(user.id)
