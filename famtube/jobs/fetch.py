import requests
from django.conf import settings
from famfetch.services import YoutubeFetchService
import logging
import os

logger = logging.getLogger(os.environ["LOGGER_NAME"])
class YoutubeSearchFetch:
    api_keys = settings.YOUTUBE_API_TOKENS

    def get_search_string():
        # can have logic to get search string
        return settings.YOUTUBE_SEARCH_STRING
    
    def get_api_key():
        current_key = YoutubeSearchFetch.api_keys.pop()
        logger.info(f"Using API key {current_key}")
        YoutubeSearchFetch.api_keys.append(current_key)
        return current_key

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
        retries_allowed = settings.YOUTUBE_RETRIES
        while(retries_allowed>0):
            try:
                response = YoutubeSearchFetch.get_latest_feed()
                if response.status_code != 200:
                    logger.error("YouTube fetch returned invalid response {}".format(response.text))
                    retries_allowed = retries_allowed-1
                    logger.info(f"YouTube fetch retrying as failed number of retries left {retries_allowed}")
                
                else:
                    # process
                    YoutubeFetchService.process_response(response.json())
                    logger.info(f"Successfully saved results")
                    break
            
            except Exception as e:
                logger.error(f"Exception occured while calling youtube fetch Exception: {e}")
                retries_allowed = retries_allowed-1