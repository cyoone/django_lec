from django.db import models

class Slides(models.Model):
    title = models.CharField(null=True, max_length=200)
    image = models.ImageField(upload_to='static/images/', blank=False)

class Good(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    category = models.CharField(null=True, max_length=200)
    image = models.ImageField(upload_to='static/good_img/', blank=False)

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