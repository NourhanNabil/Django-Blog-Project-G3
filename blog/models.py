from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Post(models.Model):
    Title = models.CharField(max_length=255)
    Image = models.ImageField()
    Content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    tags = TaggableManager()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False
    )
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.Title + " by " + str(self.author)


class ForbiddenWord(models.Model):
    forbidden_word = models.CharField(max_length=50)

    def __str__(self):
        return self.forbidden_word


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


class Reply(models.Model):
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name="replies",
        verbose_name="comment",
        null=False,
        blank=False,
    )
    content = models.TextField(
        verbose_name="blog post comment reply content", null=False, blank=False
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="replies",
        verbose_name="created by",
        null=False,
        blank=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="created at", blank=True, null=False
    )
