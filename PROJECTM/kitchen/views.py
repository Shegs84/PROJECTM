# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from kitchen.models import Post
#from kitchen.serializers import PostSerializer
#from kitchen.forms import PostForm
from rest_framework import status

# Create your views here.
from django.http import HttpResponse
def index(request):
	return HttpResponse("Hello, world. You're at the kitchen index.")

"""def home(request):
    tmpl_vars = {'form': PostForm()}
    return render(request, 'talk/index.html', tmpl_vars)

        @api_view(['GET', 'POST'])
def post_collection(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {'text': request.DATA.get('name'), 'active': request.user.pk}
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""