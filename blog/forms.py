from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment, Category


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("Title", "Image", "Content", "category", "tags", "author")
        widgets = {
            "Title": forms.TextInput(attrs={"class": "form-control"}),
            "Image": forms.FileInput(attrs={"class": "form-control"}),
            "Content": forms.Textarea(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "tags": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "value": "",
                    "id": "author-id",
                    "type": "hidden",
                }
            ),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("author", "content")
        widgets = {
            "author": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "value": "",
                    "id": "author-id",
                    "type": "hidden",
                }
            ),
            "content": forms.Textarea(attrs={"class": "form-control"}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ("category", "author")
        widgets = {
            "category": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "value": "",
                    "id": "authorId",
                    "type": "hidden",
                }
            ),
        }


class UserAdminPromoteForm(forms.Form):
    user = forms.IntegerField(
        min_value=1, required=True, help_text="user to be promoted"
    )
