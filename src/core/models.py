from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Posts

"""
One-to-One relationship
One-to-many relationship
Many-to-many relationship

CASCADE
SET_NULL
SET_DEFAULT
DO_NOTHING

"""


class Post(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title