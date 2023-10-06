from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from ..models import Post
from .serializers import PostSerializer
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from posts.models import Post
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# mysql connect
@csrf_exempt
def postApi(request, id=0):
    if request.method == 'GET':
        post=Post.objects.all()
        post_serializer=PostSerializer(post,many=True)
        return JsonResponse(post_serializer.data,safe=False)
    elif request.method == 'POST':
        post_data=JSONParser().parse(request)
        post_serializer=PostSerializer(data=post_data)
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse("added successfully",safe=False)
        return JsonResponse("Failed to add",safe=False)
    elif request.method == "PUT":
        post_data=JSONParser().parse(request)
        post=Post.objects.get(postId=post_data['postId'])
        post_serializer=PostSerializer(post,data=post_data)
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed",safe=False)
    elif request.method =='DELETE':
        post=Post.objects.get(postId=id)
        post.delete()
        return JsonResponse("Deleted Successfully",safe=False)