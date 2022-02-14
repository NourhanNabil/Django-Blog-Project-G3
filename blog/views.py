from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Category

# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .serializers import MemberSerializer
from .forms import NewUserForm, PostForm
from django.contrib.auth import login
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import CreateView , UpdateView
# like post
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse

def home(request):
    all_posts = Post.objects.all().order_by("-date")
    all_categories = Category.objects.all().order_by("category")
    context = {"posts": all_posts, "categories": all_categories}
    return render(request, "blog/home.html", context)


def postDetails(request, post_id):
    one_post = Post.objects.get(id=post_id)
    context = {"post": one_post}
    return render(request, "blog/post_details.html", context)


def categoryPosts(request, category_id):
    one_category = Category.objects.get(id=category_id)
    context = {"category": one_category}
    return render(request, "blog/category_posts.html", context)
def postDetails(request,post_id):
    one_post=Post.objects.get(id=post_id)
    total_likes = one_post.total_likes()

    liked = False
    if one_post.likes.filter(id = request.user.id).exists():
        liked = True

    context={'post':one_post, 'total_likes':total_likes, 'liked': liked}
    return render(request,'blog/post_details.html',context)


class AddPost(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/add_post.html"


class UpdatePost(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/update_post.html"


class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/delete_post.html"
    success_url = reverse_lazy("home")


def category_view(request, cats):
    all_posts = Post.objects.all().order_by("-date")
    posts = Post.objects.filter(category=cats)
    context = {"category_posts": posts}
    return render(request, "blog/categories.html", context)


def register_view(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("login")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = NewUserForm()
    return render(
        request=request,
        template_name="registration/register.html",
        context={"register_form": form},
    )


# like post view
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post-details', args=[str(pk)]))



# # rest Framework views here.
# @api_view(["GET"])
# def api_all_users(request):
#     all_users = Member.objects.all()
#     user_ser = MemberSerializer(all_users, many=True)
#     return Response(user_ser.data)


# @api_view(["GET"])
# def api_one_user(request, user_id):
#     user = Member.objects.get(id=user_id)
#     user_ser = MemberSerializer(user, many=False)
#     return Response(user_ser.data)


# @api_view(["POST"])
# def api_add_user(request):
#     user_ser = MemberSerializer(data=request.data)
#     if user_ser.is_valid():
#         user_ser.save()
#         return redirect("api-all")


# @api_view(["POST"])
# def api_edit_user(request, user_id):
#     user = Member.objects.get(id=user_id)
#     user_ser = MemberSerializer(data=request.data, instance=user)
#     if user_ser.is_valid():
#         user_ser.save()
#         return redirect("api-all")


# @api_view(["DELETE"])
# def api_del_user(request, user_id):
#     user = Member.objects.get(id=user_id)
#     user.delete()
#     return Response("User Deleted successfully!")

# def logout(request):
#     auth.logout(request)
#     return redirect('home_url')