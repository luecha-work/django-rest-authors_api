from rest_framework import status
from rest_framework.response import Response  # TODO using Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from core_apps.obreplace_app.api.serializers import WatchSerializer, StreamPlatformSerializer
from core_apps.obreplace_app.models import WatchList, StreamPlatform


class StreamPlatfromAV(APIView):
    def get(self, request):
        print("__pycache__: StreamPlat")
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WatchListAV(APIView):
    def get(self, request):
        watchs = WatchList.objects.all()
        serializer = WatchSerializer(watchs, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = WatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WatchDetailAV(APIView):
    def get(self, request, pk):
        try:
            watch = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchSerializer(watch)

        return Response(serializer.data)

    def put(self, request, pk):
        watch = WatchList.objects.get(pk=pk)
        serializer = WatchSerializer(watch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            watch = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        watch.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET'])
# def movie_list(request):
#     movies = Movie.objects.all()
#     serializer = WatchSerializer(movies, many=True)

#     return Response(serializer.data)
