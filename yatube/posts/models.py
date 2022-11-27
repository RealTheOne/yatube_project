from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Group(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title
        

class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group,
        null=True,
        blank=True,        
        on_delete=models.CASCADE
    )

