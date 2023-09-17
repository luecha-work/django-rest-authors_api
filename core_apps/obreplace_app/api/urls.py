from django.urls import path
from core_apps.obreplace_app.api.views import WatchListAV, WatchDetailAV, StreamPlatfromAV

urlpatterns = [
    path('list', WatchListAV.as_view(), name='watch-list'),
    path('<int:pk>', WatchDetailAV.as_view(), name='watch-details'),
    path('stream', StreamPlatfromAV.as_view(), name='stream-platfrom'),
    path('stream/<int:pk>', StreamPlatfromAV.as_view(), name='stream-platfrom'),

]
