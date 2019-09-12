from django.db import models
from tinymce import HTMLField, TinyMCE


class Blog_Post(models.Model):
    topic = models.CharField(max_length=250, help_text='Required')
    content = HTMLField('Content')
