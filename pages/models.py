from django.db import models

class Slides(models.Model):
    title = models.CharField(null=True, max_length=200)
    image = models.ImageField(upload_to='static/images/', blank=False)

class Good(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    category = models.CharField(null=True, max_length=200)
    image = models.ImageField(upload_to='static/good_img/', blank=False)