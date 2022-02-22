from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UserChangeForm,
    PasswordChangeForm,
)
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate


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
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")

    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    username = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password = None


class PasswordChangingForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ("old_password", "new_password1", "new_password2")

    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "type": "password"})
    )
    new_password1 = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={"class": "form-control", "type": "password"}),
    )
    new_password2 = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={"class": "form-control", "type": "password"}),
    )

    
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


class UserAuthenticationForm(AuthenticationForm):
    error_messages = AuthenticationForm.error_messages
    error_messages[
        "inactive"
    ] = "This account is blocked, please contact an admin to unblock you."

    def clean(self):
        print(self.cleaned_data)
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username is not None and password:
            self.user_cache = authenticate(
                self.request, username=username, password=password
            )
            if self.user_cache is None:
                try:
                    user_temp = User.objects.get(username=username)
                except:
                    user_temp = None

                if user_temp is not None and user_temp.check_password(password):
                    print(user_temp)
                    self.confirm_login_allowed(user_temp)
                else:
                    raise forms.ValidationError(
                        self.error_messages["invalid_login"],
                        code="invalid_login",
                        params={"username": self.username_field.verbose_name},
                    )

        return self.cleaned_data
