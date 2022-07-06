# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
#
# from .models import User
# from .serializers import UserSerializer
#
#
# @api_view(['GET'])
# def getRoutes(request):
#     routes = [
#         'GET /',
#         'GET /users',
#         'GET /users/:id',
#         'POST /users',
#     ]
#     return Response(routes)
#
#
# @api_view(['GET', 'POST'])
# def getUsers(request):
#     if request.method == 'GET':
#         users = User.objects.all()
#         if len(users) == 0:
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserForm


# после рефактроинга
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Incorrect email or password')
    return render(request, 'sign/login.html', {})


# после рефактроинга
@login_required
def logoutPage(request):
    try:
        logout(request)
    except:
        messages.error(request, 'Something wrong with logout, please try again')
    return render(request, 'sign/logout.html', {})


# после рефактроинга
@login_required
def profilePage(request):
    return render(request, 'sign/profile.html', {})


# после рефактроинга
def registerPage(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Something wrong with register, please try again')
    context = {'form': form}
    return render(request, 'sign/register.html', context)
