from django import forms
from pages.models import Post
from pages.models import Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        # fields = ['title', 'body',]
        # exclude = ['title',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']