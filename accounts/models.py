from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()  # URL to the avatar image

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ForeignKey(Avatar, on_delete=models.SET_NULL, null=True, blank=True)  # ForeignKey for avatar selection

    def __str__(self):
        return self.user.username


