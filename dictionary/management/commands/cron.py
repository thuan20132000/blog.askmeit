from django.core.management.base import BaseCommand, CommandError
import os
from crontab import CronTab


class Command(BaseCommand):
    help = 'Cron testing'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # init cron
        cron = CronTab(user=True)

        # add new cron job
        job1 = cron.new()
        job = cron.new(
            command='Users/truongthuan/Develop/python/blog/manage.py shell -c "from dictionary import schedule_cron"')

        # job settings
        job.setall("* * * * *")
        cron.write()
