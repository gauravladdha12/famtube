from rest_framework import routers
from famfetch.views import VideoDataViewSet

router = routers.SimpleRouter()

router.register(r"get_latest_videos", VideoDataViewSet, "video-data")

urlpatterns = []
urlpatterns += router.urls