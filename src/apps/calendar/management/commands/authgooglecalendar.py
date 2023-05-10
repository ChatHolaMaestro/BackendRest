import os.path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow


class Command(BaseCommand):
    help = """Authenticates the application with Google Calendar API.
    Generates a `token.json` file in the root directory of the project."""

    def handle(self, *args, **options):
        creds = None

        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(settings.GOOGLE_CALENDAR_PATH_TO_TOKEN):
            creds = Credentials.from_authorized_user_file(
                settings.GOOGLE_CALENDAR_PATH_TO_TOKEN, settings.GOOGLE_CALENDAR_SCOPES
            )
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    settings.GOOGLE_CALENDAR_PATH_TO_GOOGLE_CREDENTIALS,
                    settings.GOOGLE_CALENDAR_SCOPES,
                )
                creds = flow.run_local_server(port=0, open_browser=False)
            # Save the credentials for the next run
            with open(settings.GOOGLE_CALENDAR_PATH_TO_TOKEN, "w") as token:
                token.write(creds.to_json())

        if not creds or not creds.valid:
            raise CommandError("Could not authenticate with Google Calendar API.")
        else:
            self.stdout.write(
                self.style.SUCCESS(
                    "Successfully authenticated with Google Calendar API.\nCredentials saved in token.json."
                )
            )
