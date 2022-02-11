from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Member,Post,ForbiddenWord,Category
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MemberSerializer

def home(request):
    all_posts=Post.objects.all()
    all_categories=Category.objects.all()
    context={'posts':all_posts, 'categories':all_categories}
    return render(request,'blog/home.html',context)


def postDetails(request,post_id):
    one_post=Post.objects.get(id=post_id)
    context={'post':one_post}
    return render(request,'blog/post_details.html',context)

#rest Framework views here.
@api_view(['GET'])
def api_all_users(request):
    all_users = Member.objects.all()
    user_ser = MemberSerializer(all_users, many=True)
    return Response(user_ser.data)
@api_view(['GET'])
def api_one_user(request, user_id):
    user = Member.objects.get(id=user_id)
    user_ser = MemberSerializer(user, many=False)
    return Response(user_ser.data)
@api_view(['POST'])
def api_add_user(request):
    user_ser = MemberSerializer(data=request.data)
    if user_ser.is_valid():
        user_ser.save()
        return redirect('api-all')
@api_view(['POST'])
def api_edit_user(request, user_id):
    user= Member.objects.get(id=user_id)
    user_ser = MemberSerializer(data=request.data, instance=user)
    if user_ser.is_valid():
        user_ser.save()
        return redirect('api-all')
@api_view(['DELETE'])
def api_del_user(request, user_id):
    user= Member.objects.get(id=user_id)
    user.delete()
    return Response('User Deleted successfully!')