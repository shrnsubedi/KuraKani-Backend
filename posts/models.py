from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    votes = models.PositiveIntegerField(default=1, null=True, blank=True)

    def __str__(self):
        return self.title
