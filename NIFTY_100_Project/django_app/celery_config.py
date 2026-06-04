from celery import Celery
from celery.schedules import crontab

app = Celery(
    "nifty100"
)

app.conf.broker_url = "redis://localhost:6379/0"

app.conf.result_backend = "redis://localhost:6379/0"

app.conf.timezone = "Asia/Kolkata"

app.autodiscover_tasks(["django_app"])

app.conf.beat_schedule = {

    "run-etl-daily": {
        "task": "django_app.tasks.run_etl_pipeline",
        "schedule": crontab(hour=1, minute=0),
    },

    "score-companies-daily": {
        "task": "django_app.tasks.score_all_companies",
        "schedule": crontab(hour=2, minute=0),
    },

    "generate-pros-cons": {
        "task": "django_app.tasks.generate_pros_cons",
        "schedule": crontab(hour=2, minute=30),
    },

    "detect-anomalies-weekly": {
        "task": "django_app.tasks.detect_anomalies",
        "schedule": crontab(hour=3, minute=0, day_of_week=0),
    },

    "detect-trends-weekly": {
        "task": "django_app.tasks.detect_trends",
        "schedule": crontab(hour=3, minute=30, day_of_week=0),
    },
}