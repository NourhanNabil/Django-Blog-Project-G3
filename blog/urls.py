from django.urls import path,include
from . import views
from .views import AddPost, UpdatePost , DeletePost , AddComment
from .views import AddPost, UpdatePost , DeletePost
from .views import AddPost, UpdatePost, LikeView

urlpatterns = [
    path("", views.home, name="home"),
    path("post/<post_id>", views.postDetails, name="post-details"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/register/", views.register_view, name="register"),
    path('add_post/', AddPost.as_view(), name='add-post'),
    path('post/edit/<int:pk>', UpdatePost.as_view(), name='update-post'),
    path('post/<int:pk>/remove', DeletePost.as_view(), name='delete-post'),
    path("category/<str:cats>/", views.category_view, name="category"),
    path('post/<int:pk>/comment', AddComment.as_view(), name='add-comment'),

    # rest_framework URLs.
    # path('api-all', views.api_all_users, name='api-all'),
    # path('api-one/<user_id>', views.api_one_user, name='api-one'),
    # path('api-add', views.api_add_user, name='api-add'),
    # path('api-edit/<user_id>', views.api_edit_user, name='api-edit'),
    # path('api-del/<user_id>', views.api_del_user, name='api-del')

    # post likes url
    path('like/<int:pk>', LikeView, name='like_post')
]
 
