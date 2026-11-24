from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=120, default="Alex Rivera")
    friends_count = models.PositiveIntegerField(default=512)
    city = models.CharField(max_length=120, default="Metro City")
    school = models.CharField(
        max_length=180, default="Westfield Academy of Arts and Sciences"
    )
    profile_picture = models.ImageField(
        upload_to="profile_pictures/", blank=True, help_text="Upload a JPG or PNG photo."
    )
    profile_locked = models.BooleanField(default=True)

    def __str__(self):
        return self.name
