from django.db import models
from django.contrib.auth.models import *



class Tags(models.Model):
    topic = models.CharField(max_length=50)
    
    def __str__(self):
        return self.topic

class Animation(models.Model):
    style = models.CharField(max_length=255)

    def __str__(self):
        return self.style


class Asset(models.Model):
    file_path = models.CharField(max_length=255)
    animation = models.ForeignKey(Animation)
    image_data = models.ImageField(upload_to=None, blank=True, null=True)

    def __str__(self):
        return self.file_path

class Content(models.Model):
    text = models.CharField(max_length=10000)
    asset = models.ManyToManyField(Asset)

    def __str__(self):
        return self.text

class Author(models.Model):
    name = models.CharField(max_length =50)
    avatar = models.ForeignKey(Asset)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    content = models.ForeignKey(Content)
    title = models.CharField(max_length=255)
    post_like = models.IntegerField()
    post_type = models.CharField(max_length=255)
    date = models.DateField()
    tags = models.ManyToManyField(Tags)
    post_author = models.ForeignKey(Author)

    def __str__(self):
        return self.title







        



