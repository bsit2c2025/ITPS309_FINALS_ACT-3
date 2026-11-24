# Facebook-style Profile Page

A responsive Django profile-page clone inspired by the supplied screenshots. It includes the uploaded cyan-and-white brand mark, the dark Facebook-style navigation and profile layout, locked-profile details, an education card, highlights, a sample post, and a working profile-photo upload saved to Django's media folder.

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
DJANGO_DEBUG=true python manage.py runserver
```

Open `http://127.0.0.1:8000/`. The first page visit creates the sample profile with the details from the reference screenshot. Uploaded profile photos are stored under `media/profile_pictures/`.

## Deploy on PythonAnywhere

1. Upload the project folder to your home directory (or clone the repository there).
2. Create a virtual environment using the Python version selected for the web app, then install dependencies with `pip install -r requirements.txt`.
3. In **Web**, create a **Manual configuration** app. Set the source code and working directory to the project folder, and point the WSGI file at `profile_clone.wsgi.application`.
4. In a Bash console, run `python manage.py migrate` and `python manage.py collectstatic --noinput` from the project folder.
5. Add static mappings in **Web**: `/static/` to the `staticfiles` folder and `/media/` to the `media` folder. Reload the web app.
6. Set a private `DJANGO_SECRET_KEY` for the deployed app and set `DJANGO_ALLOWED_HOSTS` to your `username.pythonanywhere.com` hostname. Keep `DJANGO_DEBUG` unset or set it to `false`.

PythonAnywhere's manual Django deployment flow is documented in its [Deploying an existing Django project guide](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/). This activity uses SQLite and a single sample profile record.
