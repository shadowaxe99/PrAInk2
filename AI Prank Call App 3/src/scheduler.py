import schedule
import time


class Scheduler:
    def __init__(self):
        self.jobs = []

    def add_job(self, job):
        self.jobs.append(job)

    def run_jobs(self):
        while True:
            schedule.run_pending()
            time.sleep(1)