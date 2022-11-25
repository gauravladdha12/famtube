import requests
from django.conf import settings
from famfetch.services import YoutubeFetchService
import logging
import os

logger = logging.getLogger(os.environ["LOGGER_NAME"])
class YoutubeSearchFetch:
    def get_search_string():
        # can have logic to get search string
        return settings.YOUTUBE_SEARCH_STRING
    
    def get_api_key():
        # can have logic to get api key
        return settings.YOUTUBE_API_TOKEN

    def get_latest_feed():
        api_endpoint = "https://www.googleapis.com/youtube/v3/search"
        params = {
            'part': 'snippet',
            'q': YoutubeSearchFetch.get_search_string(), 
            'key': YoutubeSearchFetch.get_api_key(),
            'maxResults': settings.MAX_YOUTUBE_SEARCH_RESULT,
            'type': 'video' 
        }
        return requests.get(api_endpoint, params=params)

    def fetch():
        response = YoutubeSearchFetch.get_latest_feed()

        if response.status_code != 200:
            # log error response
            logger.error("YouTube fetch returned invalid response {}".format(response.text))
            
        # process
        YoutubeFetchService.process_response(response.json())

