from django.contrib import admin
from django.urls import path, include
from jobs import executor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('famfetch.urls')),
]

# initializing scheduler
executor.start()