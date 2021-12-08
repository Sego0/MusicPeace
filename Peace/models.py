from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import TextField
from django.utils import timezone

class Profile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(default="Hola, MusicPeace", max_length=100)
    image = models.ImageField(default="default.png")

    def __str__(self):
        return f"Perfil de {self.User.username}"

class Post(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post")

    class  Meta:
        ordering = ["-timestamp"]

        def __str__(self):
            return self.content        
# Create your models here.
