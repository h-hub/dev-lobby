from django.shortcuts import render
from blogPostManagement.forms import BlogPostCreateForm


def create(request):
    if request.method == 'POST':
        form = BlogPostCreateForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.save()
    else:
        form = BlogPostCreateForm()
    return render(request, 'blogPostManagement/create_blog_form.html', {'form': form})