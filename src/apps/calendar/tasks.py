import os.path

from django.conf import settings

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

from config import celery_app


@celery_app.task
def create_calendar_event():
    if not os.path.exists(settings.GOOGLE_CALENDAR_PATH_TO_TOKEN):
        raise Exception(
            "Could not find token.json file. Authenticate with `manage.py authgooglecalendar`"
        )

    creds = Credentials.from_authorized_user_file(
        settings.GOOGLE_CALENDAR_PATH_TO_TOKEN, settings.GOOGLE_CALENDAR_SCOPES
    )
    if not creds or not creds.valid:
        raise Exception(
            "Credentials are invalid. Authenticate with `manage.py authgooglecalendar`"
        )

    service = build("calendar", "v3", credentials=creds)
