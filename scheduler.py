from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from main import run_spiders


def job():
    print('\n' + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    run_spiders()


# BlockingScheduler
scheduler = BlockingScheduler()
scheduler.add_job(job, 'cron', minute='*/1')
scheduler.start()
