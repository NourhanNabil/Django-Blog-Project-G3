from django import forms
from django.contrib.auth.forms import UserCreationForm , UserChangeForm , PasswordChangeForm
from django.contrib.auth.models import User
from .models import ForbiddenWord, Post, Comment, Category


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



class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    first_name= forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name= forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class": "form-control"}))
    username= forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ("username","first_name","last_name", "email", "password")


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control" , "type" : "password"}))
    new_password1= forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class": "form-control" , "type" : "password"}))
    new_password2= forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class": "form-control", "type" : "password"}))
    
    class Meta:
        model = User
        fields = ("old_password","new_password1","new_password2")

class ForbiddenWordForm(forms.ModelForm):
    class Meta:
        model = ForbiddenWord
        fields = ("forbidden_word", "author")
        widgets = {
            "forbidden_word": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "value": "",
                    "id": "admin-Id",
                    "type": "hidden",
                }
            ),
        }