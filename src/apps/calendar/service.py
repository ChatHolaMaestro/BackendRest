import os.path
import datetime

from django.conf import settings

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


class CalendarServiceException(Exception):
    pass


def build_calendar_service():
    """Builds a service object for interacting with the Calendar API.

    Returns:
        A service object for interacting with the Calendar API.

    Raises:
        CalendarServiceException: If the credentials are invalid.
    """

    if not os.path.exists(settings.GOOGLE_CALENDAR_PATH_TO_TOKEN):
        raise CalendarServiceException(
            "Could not find token.json file. Authenticate with `manage.py authgooglecalendar`"
        )

    try:
        creds = Credentials.from_authorized_user_file(
            settings.GOOGLE_CALENDAR_PATH_TO_TOKEN, settings.GOOGLE_CALENDAR_SCOPES
        )
    except Exception as e:
        raise CalendarServiceException(f"Could not read credentials. Error: {e}")

    if creds.expired:
        try:
            creds.refresh(Request())
        except Exception as e:
            raise CalendarServiceException(f"Could not refresh credentials. Error: {e}")

        # Save the credentials for the next run
        with open(settings.GOOGLE_CALENDAR_PATH_TO_TOKEN, "w") as token:
            token.write(creds.to_json())

    return build("calendar", "v3", credentials=creds)


def get_calendar_id() -> str:
    """Get the calendar id from the file.

    Returns:
        The calendar id.

    Raises:
        CalendarServiceException: If the calendar id file does not exist.
    """
    if not os.path.exists(settings.GOOGLE_CALENDAR_PATH_TO_CALENDAR_ID):
        raise CalendarServiceException(
            "Could not find calendar id file. Select one with `manage.py selectgooglecalendar`"
        )

    with open(settings.GOOGLE_CALENDAR_PATH_TO_CALENDAR_ID, "r") as calendar_id_file:
        return calendar_id_file.read().strip()


def build_calendar_event(
    summary: str, description: str, start: str, end: str, attendees: list[str]
) -> dict:
    """Build a calendar event object.

    Args:
        summary (str): title of the event.
        description (str): description of the event.
        start (str): start datetime of the event. Format: YYYY-MM-DDTHH:MM:SS
        end (str): end datetime of the event. Format: YYYY-MM-DDTHH:MM:SS
        attendees (list[str]): list of emails of the attendees.

    Returns:
        dict: A calendar event object.

    Raises:
        CalendarServiceException: If the start or end datetime are not in the correct format.
    """

    try:
        datetime.datetime.fromisoformat(start)
    except ValueError:
        raise CalendarServiceException(
            "The start date must be in the format YYYY-MM-DDThh:mm:ss"
        )
    try:
        datetime.datetime.fromisoformat(end)
    except ValueError:
        raise CalendarServiceException(
            "The end date must be in the format YYYY-MM-DDThh:mm:ss"
        )

    event = {
        "summary": summary,
        "start": {
            "dateTime": start,
            "timeZone": "America/Bogota",
        },
        "end": {
            "dateTime": end,
            "timeZone": "America/Bogota",
        },
        "attendees": [{"email": attendee} for attendee in attendees],
        "reminders": {
            "useDefault": False,
            "overrides": [
                {"method": "email", "minutes": 30},
                {"method": "popup", "minutes": 10},
            ],
        },
    }
    if description and description.strip() != "":
        event["description"] = description

    return event
