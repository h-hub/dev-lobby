from django.forms import ModelForm, forms
from .models import Blog_Post


class BlogPostCreateForm(ModelForm):

    class Meta:
        model = Blog_Post
        fields = ('topic', 'content' )