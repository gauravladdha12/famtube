from django.db import models

class videos(models.Model):
    id = models.BigAutoField(
        editable=False,
        primary_key=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    title = models.TextField()

    description = models.TextField()

    publish_date_time = models.DateTimeField(null=False)

    thumbnail_url = models.URLField(max_length=1000, blank=True, null=True)