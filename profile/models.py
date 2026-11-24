from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=120, default="Joshua Agawin")
    friends_count = models.PositiveIntegerField(default=373)
    city = models.CharField(max_length=120, default="Lucena City")
    school = models.CharField(
        max_length=180, default="DepEd Quezon National High School"
    )
    profile_picture = models.ImageField(
        upload_to="profile_pictures/", blank=True, help_text="Upload a JPG or PNG photo."
    )
    profile_locked = models.BooleanField(default=True)

    def __str__(self):
        return self.name
