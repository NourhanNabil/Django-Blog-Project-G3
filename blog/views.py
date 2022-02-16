from sre_constants import SUCCESS
from django.shortcuts import render, redirect
from .models import Post, Category , Comment
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import (
    NewUserForm,
    PostForm,
    CommentForm,
    CategoryForm,
    UserAdminPromoteForm,
    EditProfileForm,
    PasswordChangingForm,
)
from django.contrib.auth import login
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# like post
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import PasswordChangeView



def home(request):
    all_posts = Post.objects.all().order_by('-date')
    all_categories = Category.objects.all()
    all_subs = Category.subscribes.through.objects.filter(user_id = request.user.id)
    list_of_subs = []
    for sub in all_subs:
        list_of_subs.append(sub.category_id)
    context = {"posts": all_posts, "categories": all_categories,'user_id': request.user.id, 'list_of_subs': list_of_subs}
    return render(request, "blog/home.html", context)


def postDetails(request, post_id):
    one_post = Post.objects.get(id=post_id)
    total_likes = one_post.total_likes()
    liked = False
    if one_post.likes.filter(id = request.user.id).exists():
        liked = True
    context = {"post": one_post,'total_likes':total_likes, 'liked': liked}
    return render(request, "blog/post_details.html", context)


def categoryPosts(request, category_id):
    one_category = Category.objects.get(id=category_id)
    context = {"category": one_category}
    return render(request, "blog/category_posts.html", context)

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


class AddComment(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/add_comment.html"

    def form_valid(self, form):
        form.instance.post_id = self.kwargs["pk"]
        return super().form_valid(form)

def category_view(request, cats):
    posts = Post.objects.filter(category=cats).order_by("-date")
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
    # post_id as the submit button name
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse("post-details", args=[str(pk)]))

def search_bar(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        result = Post.objects.filter(name__contains=searched)
        return render(
            request, "blog/search_bar.html", {"searched": searched, "result": result}
        )
    else:
        return render(request, "blog/search_bar.html", {})


# subscribe to category view
def subView(request, pk):
    # category_id as the submit button name
    category = get_object_or_404(Category, id=request.POST.get('category_id'))
    subscribed = False
    if category.subscribes.filter(id = request.user.id).exists():
        category.subscribes.remove(request.user)
        subscribed = False
    else:
        category.subscribes.add(request.user)
        subscribed = True
    return redirect('/')


def AdminPage(request):
    return render(request, "admin-pages/admin_all.html")


def ManageUsers(request):
    users = User.objects.all().order_by("id")
    context = {"users": users}
    return render(request, "admin-pages/admin_users.html", context)


def ManagePosts(request):
    posts = Post.objects.all().order_by("-date")
    context = {"posts": posts}
    return render(request, "admin-pages/admin_posts.html", context)


def ManageCategories(request):
    all_categories = Category.objects.all().order_by("-date")
    context = {"all_categories": all_categories}
    return render(request, "admin-pages/admin_categories.html", context)


def ManageWords(request):
    return render(request, "admin-pages/admin_words.html")


class AddCategory(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "admin-pages/add_category.html"
    success_url = reverse_lazy("manage-Categories")


class UpdateCategory(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "admin-pages/update_category.html"
    success_url = reverse_lazy("manage-Categories")


class DeleteCategory(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = "admin-pages/delete_category.html"
    success_url = reverse_lazy("manage-Categories")


def promote_user_view(request):
    if request.method == "POST":
        form = UserAdminPromoteForm(request.POST)
        print(form.data)
        if form.is_valid():
            user = User.objects.get(pk=form.cleaned_data["user"])
            user.is_staff = True
            user.save()
            return redirect("manage-users")
    return HttpResponse("", status=403)


class UserEditView(UpdateView):
    form_class=EditProfileForm
    template_name="registration/edit_profile.html"
    success_url= reverse_lazy('home')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class=PasswordChangingForm
    template_name="registration/change_password.html"
    success_url= reverse_lazy('password-success')

def PasswordChanged(request):
    return render(request, "registration/Password_successfully.html")