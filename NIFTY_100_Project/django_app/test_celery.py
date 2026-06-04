from django_app.celery_config import app

result = app.send_task("django_app.tasks.score_all_companies")

print("Task sent!")
print(result.id)