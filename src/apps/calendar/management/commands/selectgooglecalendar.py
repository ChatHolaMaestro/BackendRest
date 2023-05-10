import os.path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


class Command(BaseCommand):
    help = """Authenticates the application with Google Calendar API.
    Generates a `token.json` file in the root directory of the project."""

    def handle(self, *args, **options):
        if not os.path.exists(settings.GOOGLE_CALENDAR_PATH_TO_TOKEN):
            raise CommandError(
                "Could not find token.json file. Authenticate with `manage.py authgooglecalendar`"
            )

        creds = Credentials.from_authorized_user_file(
            settings.GOOGLE_CALENDAR_PATH_TO_TOKEN, settings.GOOGLE_CALENDAR_SCOPES
        )
        if not creds or not creds.valid:
            raise CommandError(
                "Credentials are invalid. Authenticate with `manage.py authgooglecalendar`"
            )

        try:
            service = build("calendar", "v3", credentials=creds)

            calendar_list = service.calendarList().list(maxResults=250).execute()

            self.stdout.write(
                self.style.HTTP_INFO("Select a calendar from the list below:")
            )
            i = 0
            for calendar_list_entry in calendar_list["items"]:
                self.stdout.write(
                    self.style.HTTP_INFO(
                        "{}. {} - ID: {}".format(
                            i + 1,
                            calendar_list_entry["summary"],
                            calendar_list_entry["id"],
                        )
                    )
                )
                i += 1
            self.stdout.write(
                self.style.HTTP_INFO(
                    "{}. Create a new calendar".format(len(calendar_list["items"]) + 1)
                )
            )
            self.stdout.write(
                self.style.HTTP_INFO(
                    "{}. Cancel".format(len(calendar_list["items"]) + 2)
                )
            )

            while True:
                calendar_number = int(
                    input("Enter the # of the calendar you want to use: ")
                )
                if (
                    calendar_number > 0
                    and calendar_number <= len(calendar_list["items"]) + 2
                ):
                    break

            if calendar_number == len(calendar_list["items"]) + 2:
                self.stdout.write(self.style.NOTICE("Cancelled"))
                return

            if calendar_number == len(calendar_list["items"]) + 1:
                calendar_summary = input("Enter the name of the new calendar: ")
                calendar_list_entry = (
                    service.calendars()
                    .insert(body={"summary": calendar_summary})
                    .execute()
                )
                calendar_id = calendar_list_entry["id"]
            else:
                calendar_id = calendar_list["items"][calendar_number - 1]["id"]

            with open(
                settings.GOOGLE_CALENDAR_PATH_TO_CALENDAR_ID, "w"
            ) as calendar_id_file:
                calendar_id_file.write(calendar_id)

        except Exception as e:
            raise CommandError(
                "Could not connect to Google Calendar API. Error: {}".format(e)
            )
