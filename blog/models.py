from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager
from django.urls import reverse
from ckeditor.fields import RichTextField

class Category(models.Model):
    category = models.CharField(max_length=50,unique=True)
    subscribes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='category_subscribes')
   
    def total_subscribes(self):
        return self.subscribes.count()

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.category


class Post(models.Model):
    Title = models.CharField(max_length=255)
    Image = models.ImageField(null=True, upload_to="images/")
    Content = RichTextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    tags = TaggableManager(blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False
    )
    date = models.DateTimeField(auto_now_add=True, null=True)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="blog_posts", blank=True
    )

    # total numbers of likes to be shown in the post
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.Title + " by " + str(self.author)

    # to redirect when adding post or updating post 
    def get_absolute_url(self):
        return reverse("post-details", args=[str(self.pk)])


class ForbiddenWord(models.Model):
    forbidden_word = models.CharField(max_length=50, unique=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.forbidden_word

    def save(self, *args, **kwargs) -> None:

        self.forbidden_word = self.forbidden_word.strip()
        return super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="comment",
        null=False,
        blank=False,
    )
    content = models.TextField(
        verbose_name="blog post comment content", null=False, blank=False
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="author",
        null=False,
        blank=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="created at", blank=True, null=False
    )
     
     # to make the comment appear with author name and post title
    def __str__(self):
        return "%s - %s" % (self.post.Title, self.author)

    # to redirect when adding comment or updating comment 
    def get_absolute_url(self):
        return reverse("post-details", args=[str(self.post.pk)])

