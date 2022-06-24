from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /',
        'GET /users',
        'GET /users/:id'
    ]
    return Response(routes)


@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
