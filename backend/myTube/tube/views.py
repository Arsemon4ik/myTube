from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Video
from .serializers import VideoSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/videos',
        'GET /api/videos/:id'
    ]
    return Response(routes)


@api_view(['GET'])
def getVideos(request):
    videos = Video.objects.all()
    serializer = VideoSerializer(videos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getVideo(request, pk):
    videos = Video.objects.get(id=pk)
    serializer = VideoSerializer(videos, many=False)
    return Response(serializer.data)
