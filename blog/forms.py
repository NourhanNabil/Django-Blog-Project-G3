from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post


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
        model=Post
        fields=("Title","Image","Content","category","tags","author")
        widgets={
            'Title':forms.TextInput(attrs={'class':'form-control'}),
            'Image':forms.FileInput(attrs={'class':'form-control'}),
            'Content':forms.Textarea(attrs={'class':'form-control'}),
            'category':forms.TextInput(attrs={'class':'form-control'}),
            'tags':forms.TextInput(attrs={'class':'form-control'}),  
            'author':forms.Select(attrs={'class':'form-control'}),
        }