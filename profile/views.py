from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .forms import ProfilePictureForm
from .models import Profile


@require_http_methods(["GET", "POST"])
def profile_page(request):
    profile, _ = Profile.objects.get_or_create(pk=1)

    if request.method == "POST":
        form = ProfilePictureForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile picture has been updated.")
            return redirect("profile")
        messages.error(request, "Please choose a valid image and try again.")
    else:
        form = ProfilePictureForm(instance=profile)

    return render(request, "profile/profile.html", {"profile": profile, "form": form})
