import logging
import os
from famfetch.models import videos

logger = logging.getLogger(os.environ["LOGGER_NAME"])

class YoutubeFetchService:
    def process_response(response):
        response = response['items']
        videosDO = YoutubeFetchService.create_video_data_object(response)
        videos.objects.bulk_create(videosDO)

    
    def create_video_data_object(response):
        videosDO = []
        for data in response:
            videosDO.append(
                videos(
                    title = data['snippet']['title'],
                    description = data['snippet']['description'],
                    publish_date_time = data['snippet']['publishTime'],
                    thumbnail_url = data['snippet']['thumbnails']['default']['url']
                )
            )
        return videosDO