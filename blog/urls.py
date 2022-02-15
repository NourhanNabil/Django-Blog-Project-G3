from django.urls import path,include
from . import views
from .views import AddPost, UpdatePost , DeletePost , AddComment , AddCategory, UpdateCategory ,DeleteCategory
from .views import AddPost, UpdatePost, LikeView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", views.home, name="home"),
    path("post/<post_id>", views.postDetails, name="post-details"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/register/", views.register_view, name="register"),
    path('add_post/', AddPost.as_view(), name='add-post'),
    path('post/edit/<int:pk>', UpdatePost.as_view(), name='update-post'),
    path('post/<int:pk>/remove', DeletePost.as_view(), name='delete-post'),
    path("category/<str:cats>/", views.category_view, name="category"),
    path("search_bar", views.search_bar, name="search-bar"),
    path('post/<int:pk>/comment', AddComment.as_view(), name='add-comment'),
    path('manage-blog', views.AdminPage, name="manage-blog"),
    path('manage-blog/users', views.ManageUsers, name="manage-users"),
    path('manage-blog/posts', views.ManagePosts, name="manage-posts"),
    path('manage-blog/Categories', views.ManageCategories, name="manage-Categories"),
    path('manage-blog/forbidden-words', views.ManageWords, name="manage-forbidden-words"),
    path('manage-blog/Categories/Add', AddCategory.as_view(), name='add-category'),
    path('manage-blog/Categories/edit/<int:pk>', UpdateCategory.as_view(), name='update-category'),
    path('manage-blog/Categories/delete/<int:pk>', DeleteCategory.as_view(), name='delete-category'),

    # rest_framework URLs.
    # path('api-all', views.api_all_users, name='api-all'),
    # path('api-one/<user_id>', views.api_one_user, name='api-one'),
    # path('api-add', views.api_add_user, name='api-add'),
    # path('api-edit/<user_id>', views.api_edit_user, name='api-edit'),
    # path('api-del/<user_id>', views.api_del_user, name='api-del')
    # post likes url
    path('like/<int:pk>', LikeView, name='like_post')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
 
