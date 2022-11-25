from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from famfetch.models import videos
from famfetch.serializers import VideosSerializer
from django.http import JsonResponse
from django.core.paginator import Paginator


class VideoDataViewSet(viewsets.ViewSet):
    def get_queryset(self):
        return videos.objects.all().order_by("-publish_date_time", "-id")

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            pagination = PageNumberPagination()
            pagination.page_size = 10
            page = pagination.paginate_queryset(queryset, request)
            data = VideosSerializer(page, many=True).data
            return pagination.get_paginated_response(data)
        except Exception as e:
            return JsonResponse(
                {
                    "type": type(e).__name__,
                    "message": str(e),
                    "code": "INTERNAL_ERROR",
                    "extra": {},
                },
                status=500,
            )
