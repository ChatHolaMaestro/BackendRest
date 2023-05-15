import os
from celery import Celery
from celery.schedules import crontab

from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("chat_hola_maestro")


# Configure the beat scheduler to run the clean_up_calendar_events task every day at 00:00
app.conf.beat_schedule = {
    "clean-up-calendar-events": {
        "task": "apps.calendar.tasks.clean_up_calendar_events",
        "schedule": crontab(hour=0, minute=0),
    }
}


app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
