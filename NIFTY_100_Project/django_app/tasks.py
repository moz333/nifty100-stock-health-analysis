from celery import shared_task
import time

@shared_task(name="django_app.tasks.run_etl_pipeline")
def run_etl_pipeline():

    print("Running ETL pipeline")

    return "ETL completed"


@shared_task(name="django_app.tasks.score_all_companies")
def score_all_companies():


    print("=== TASK STARTED ===", flush=True)

    time.sleep(5)

    print("Calculating health scores", flush=True)

    return "Scores updated"


@shared_task(name="django_app.tasks.generate_pros_cons")
def generate_pros_cons():

    print("Generating pros and cons")

    return "Pros/Cons generated"


@shared_task(name="django_app.tasks.detect_anomalies")

def detect_anomalies():

    print("Running anomaly detection")

    return "Anomalies detected"


@shared_task(name="django_app.tasks.detect_trends")
def detect_trends():

    print("Running trend analysis")

    return "Trend analysis completed"


@shared_task(name="django_app.tasks.invalidate_cache")
def invalidate_cache():

    print("Invalidating Redis cache")

    return "Cache cleared"