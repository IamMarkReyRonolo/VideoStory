from django.db import models
from api.users.models import User

# Create your models here.


class VideoPost(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_url = models.CharField(max_length=255)
    thumbnail_url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = (
            "-updated_at",
            "-created_at",
        )

    def __str__(self):
        return self.title
