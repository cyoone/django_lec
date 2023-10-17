from django.db import models
from django.contrib.auth.models import User

class Slides(models.Model):
    title = models.CharField(null=True, max_length=200)
    image = models.ImageField(upload_to='static/images/', blank=False)

class Good(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    category = models.CharField(null=True, max_length=200)
    image = models.ImageField(upload_to='static/good_img/', blank=False)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')

class New(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    category = models.CharField(null=True, max_length=200)
    image = models.ImageField(upload_to='static/new_img/', blank=False)

class Best(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    category = models.CharField(null=True, max_length=200)
    image = models.ImageField(upload_to='static/best_img/', blank=False)

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content_list = models.ForeignKey(Good, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)