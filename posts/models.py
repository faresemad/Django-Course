from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE , related_name='posts_author')
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000, blank=True, null=True)
    images = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, null=True)
    active = models.BooleanField(default=False)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title