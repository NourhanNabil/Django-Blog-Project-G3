from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<post_id>', views.postDetails, name='post-details'),
 ]