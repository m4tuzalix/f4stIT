import random
from celery import shared_task
from scraper.starter import Starter
from .models import Job

@shared_task(name="scrap_jobs")
def scraper():
    starter = Starter()
    data = starter.start_fetching()
    for single_job in data:
        job, created = Job.objects.get_or_create(
            link = single_job[0],
            position = single_job[1],
            city = single_job[2]
        )