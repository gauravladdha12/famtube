from apscheduler.schedulers.background import BackgroundScheduler
from jobs.fetch import YoutubeSearchFetch
from django.conf import settings

def start():
	scheduler = BackgroundScheduler()
	scheduler.add_job(YoutubeSearchFetch.fetch, 'interval', seconds=settings.YOUTUBE_FETCH_INTERVAL)
	scheduler.start()