from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profilepic.png', upload_to='profile_pictures')
    location = models.TextField(max_length=300)

    def __str__(self):
        return self.user.username