from .models import Ad, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active, user.is_activated = False, False
        user.save()
        return user

class AdForm(forms.ModelForm):

    class Meta:
        model = Ad
        fields = ['title', 'info', 'img']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']

