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

# Screenshots

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/ca233373-f6b5-4403-bc58-dfdd469053c4" />

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/3ee0c189-4d4c-4203-a43d-d64b0a8002b3" />

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/e4dd2db8-2069-4a68-8a62-f2e6e9059fcd" />


Testing of the feature of uploading the profile picture

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/b4be60c2-cf3a-46d6-a18d-2b2693fd7aef" />

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/8218165b-bc3a-4ecf-b0f4-aadd0e9d7bc7" />



