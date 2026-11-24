from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="Joshua Agawin", max_length=120)),
                ("friends_count", models.PositiveIntegerField(default=373)),
                ("city", models.CharField(default="Lucena City", max_length=120)),
                (
                    "school",
                    models.CharField(
                        default="DepEd Quezon National High School", max_length=180
                    ),
                ),
                (
                    "profile_picture",
                    models.ImageField(
                        blank=True,
                        help_text="Upload a JPG or PNG photo.",
                        upload_to="profile_pictures/",
                    ),
                ),
                ("profile_locked", models.BooleanField(default=True)),
            ],
        ),
    ]
