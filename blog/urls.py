from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("post/<post_id>", views.postDetails, name="post-details"),
    path("accounts/register/", views.register_view, name="register"),
    path("accounts/login/", views.UserLoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path(
        "accounts/password_change/",
        auth_views.PasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "accounts/password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path(
        "accounts/password_reset/",
        auth_views.PasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        "accounts/password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "accounts/reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "accounts/reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path("add_post/", AddPost.as_view(), name="add-post"),
    path("post/edit/<int:pk>", UpdatePost.as_view(), name="update-post"),
    path("post/<int:pk>/remove", DeletePost.as_view(), name="delete-post"),
    path("category/<str:cats>/", views.category_view, name="category"),
    path("search_bar", views.search_bar, name="search-bar"),
    path("post/<int:pk>/comment", AddComment.as_view(), name="add-comment"),
    path("post/comment/edit/<int:pk>", UpdateComment.as_view(), name="update-comment"),
    path(
        "post/comment/<int:pk>/remove", DeleteComment.as_view(), name="delete-comment"
    ),
    path("manage-blog", views.AdminPage, name="manage-blog"),
    path("manage-blog/users", views.ManageUsers, name="manage-users"),
    path("manage-blog/posts", views.ManagePosts, name="manage-posts"),
    path("manage-blog/Categories", views.ManageCategories, name="manage-Categories"),
    path(
        "manage-blog/forbidden-words", views.ManageWords, name="manage-forbidden-words"
    ),
    # admin manage-categories
    path("manage-blog/Categories/Add", AddCategory.as_view(), name="add-category"),
    path(
        "manage-blog/Categories/edit/<int:pk>",
        UpdateCategory.as_view(),
        name="update-category",
    ),
    path(
        "manage-blog/Categories/delete/<int:pk>",
        DeleteCategory.as_view(),
        name="delete-category",
    ),
    path("manage-blog/users/promote/", views.promote_user_view, name="promote-user"),
    path("manage-blog/users/block/", views.block_user_view, name="block-user"),
    # post likes url
    path("like/<int:pk>", LikeView, name="like_post"),
    # post edit-profile
    path("accounts/edit-profile/", UserEditView.as_view(), name="edit-profile"),
    path("accounts/password/", PasswordsChangeView.as_view(), name="change-password"),
    path("accounts/password_success/", views.PasswordChanged, name="password-success"),
    # category subscribe url
    path("subscribe/<int:pk>", subView, name="subscribe"),
    # admin manage-forbidden-words
    path("manage-blog/words/Add", AddForbbidenWord.as_view(), name="add-word"),
    path(
        "manage-blog/words/edit/<int:pk>",
        UpdateForbbidenWord.as_view(),
        name="update-word",
    ),
    path(
        "manage-blog/words/delete/<int:pk>",
        DeleteForbbidenWord.as_view(),
        name="delete-word",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
