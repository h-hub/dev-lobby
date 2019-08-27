from django.conf.urls import url
from django.urls import include

from . import views

urlpatterns = [
    url('create/', views.create, name='create_blog_post'),
]
