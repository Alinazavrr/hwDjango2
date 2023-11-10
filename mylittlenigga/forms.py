from django import forms
from .models import Ad, Comment

class AdForm(forms.ModelForm):

    class Meta:
        model = Ad
        fields = ['title', 'info', 'img']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']

