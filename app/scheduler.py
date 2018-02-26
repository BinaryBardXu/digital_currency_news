from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from . import spiders_runner


def job():
    print('\n' + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    spiders_runner.run()


# BlockingScheduler
scheduler = BlockingScheduler()
scheduler.add_job(job, 'cron', minute='*/1')
scheduler.start()
