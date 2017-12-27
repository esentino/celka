import os
from random import randint
from celery import Celery
from celery.schedules import crontab
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celka.settings')

app = Celery('celka')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.on_after_configure.connect
def setup_schedule_tasks(sender, **kwargs):
    # Run task every 5 seconds with name Roll the dice
    sender.add_periodic_task(5.0, roll_the_dice.s(), name="Roll the dice by 5s")
    # Run task every 7 secodns end atfer 5 run.
    sender.add_periodic_task(7.0, roll_the_dice.s(), expire=5, name="Roll the dice by 7s 5 times")
    # Run task every 2 minutes
    sender.add_periodic_task(crontab(minute='*/2'), roll_the_dice.s(), name="Roll the dice every 2 minutes")


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

@app.task
def roll_the_dice():
    return randint(1, 6)
