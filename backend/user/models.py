from django.db import models


class UserProfile(models.Model):
    bio = models.CharField(max_length=40, blank=True)
    profile_image = models.URLField(max_length=200, blank=True)
