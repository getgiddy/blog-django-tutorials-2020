from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()


class User(models.Model):
    username = models.CharField(max_length=250)
    email = models.EmailField()
    password = models.CharField(max_length=250)