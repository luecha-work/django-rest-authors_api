from django.urls import path
from core_apps.obreplace_app.api.views import WatchListAV, StreamPlatformDetailAV, WatchDetailAV, StreamPlatformAV

urlpatterns = [
    path('list', WatchListAV.as_view(), name='watch-list'),
    path('list/<int:pk>', WatchDetailAV.as_view(), name='watch-details'),
    path('stream', StreamPlatformAV.as_view(), name='stream-list'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-platfrom'),

]
