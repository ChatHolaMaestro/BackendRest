FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED ${PYTHONUNBUFFERED:-1}
ENV PYTHONDONTWRITEBYTECODE ${PYTHONDONTWRITEBYTECODE:-1}

WORKDIR /app

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/* \
  && useradd --create-home python \
  && chown -R python:python /app

USER python

# Requirements are installed here to ensure they will be cached.
COPY --chown=python:python ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY --chown=python:python ./compose/local/django/entrypoint /entrypoint
RUN chmod +x /entrypoint

COPY --chown=python:python ./compose/local/django/start /start
RUN chmod +x /start

COPY --chown=python:python ./compose/local/django/celery/worker/start /start-celeryworker
RUN chmod +x /start-celeryworker

COPY --chown=python:python ./compose/local/django/celery/beat/start /start-celerybeat
RUN chmod +x /start-celerybeat

COPY --chown=python:python ./compose/local/django/celery/flower/start /start-flower
RUN chmod +x /start-flower

WORKDIR /app/src

ENTRYPOINT ["/entrypoint"]
