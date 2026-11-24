from django import forms

from .models import Profile


class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("profile_picture",)
        widgets = {
            "profile_picture": forms.FileInput(
                attrs={"accept": "image/*", "class": "visually-hidden", "id": "profile-photo-input"}
            )
        }

    def clean_profile_picture(self):
        image = self.cleaned_data.get("profile_picture")
        if image and image.size > 5 * 1024 * 1024:
            raise forms.ValidationError("Choose an image smaller than 5 MB.")
        return image
