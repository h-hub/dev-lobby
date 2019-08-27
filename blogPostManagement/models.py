from django.db import models


class Blog_Post(models.Model):
    topic = models.CharField(max_length=30, help_text='Required')
    content = models.TextField(help_text='Required')
