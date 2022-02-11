from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Member,Post,ForbiddenWord,Category


def home(request):
    all_posts=Post.objects.all()
    all_categories=Category.objects.all()
    context={'posts':all_posts, 'categories':all_categories}
    return render(request,'blog/home.html',context)


def postDetails(request,post_id):
    one_post=Post.objects.get(id=post_id)
    context={'post':one_post}
    return render(request,'blog/post_details.html',context)

