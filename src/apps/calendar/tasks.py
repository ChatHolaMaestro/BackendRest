import os.path

from django.conf import settings

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

from config import celery_app


def build_calendar_service():
    if not os.path.exists(settings.GOOGLE_CALENDAR_PATH_TO_TOKEN):
        raise Exception(
            "Could not find token.json file. Authenticate with `manage.py authgooglecalendar`"
        )

    creds = Credentials.from_authorized_user_file(
        settings.GOOGLE_CALENDAR_PATH_TO_TOKEN, settings.GOOGLE_CALENDAR_SCOPES
    )

    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
        # Save the credentials for the next run
        with open(settings.GOOGLE_CALENDAR_PATH_TO_TOKEN, "w") as token:
            token.write(creds.to_json())
    else:
        raise Exception(
            "Credentials are invalid. Authenticate with `manage.py authgooglecalendar`"
        )

    return build("calendar", "v3", credentials=creds)


@celery_app.task
def create_calendar_event():
    service = build_calendar_service()
