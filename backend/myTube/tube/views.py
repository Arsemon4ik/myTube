# @api_view(['GET'])
# def getRoutes(request):
#     routes = [
#         'GET /',
#         'GET /videos',
#         'GET /videos/:id',
#         'PUT /videos/:id',
#         'DELETE /videos/:id',
#         'POST /videos',
#     ]
#     return Response(routes)
#
#
# @api_view(['GET', 'POST'])
# def getVideos(request):
#     if request.method == 'GET':
#         videos = Video.objects.all()
#         if len(videos) == 0:
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         serializer = VideoSerializer(videos, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = VideoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def getVideo(request, pk):
#     try:
#         video = Video.objects.get(id=pk)
#     except Video.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         videos = Video.objects.get(id=pk)
#         serializer = VideoSerializer(videos, many=False)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = VideoSerializer(video, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         video.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

from django.contrib import messages
from django.shortcuts import render, redirect

from .filters import VideoFilter
# Create your views here.
from .forms import *
from .models import Comment, Subscribe, Author
from django.conf import settings
from django.db.models import Q
from sign.models import User


def indexPage(request):

    queryDict = request.GET
    query = queryDict.get('q')
    if query is not None:
        videos = Video.objects.filter(
            Q(videoHeader__icontains=query)
        )
    else:
        videos = Video.objects.all()
    context = {'videos': videos}
    return render(request, 'tube/index.html', context)


def postLikePage(request, pk):
    user = request.user
    try:
        video = Video.objects.get(id=pk)
        if user in video.videoUsersLiked.all():
            messages.error(request, 'You have already liked this video!')
            return redirect('post_detail', pk=video.id)
        else:
            video.videoUsersLiked.add(user)
        video.like()
        video.save()
        return redirect('post_detail', pk=video.id)
    except:
        video = Video.objects.get(id=pk)
        messages.error(request, 'Something wrong with post')
        return redirect('post_detail', pk=video.id)

    return render(request, 'tube/videoDetail.html', {})


def postDisLikePage(request, pk):
    user = request.user
    try:
        video = Video.objects.get(id=pk)
        if user in video.videoUsersDisLiked.all():
            messages.error(request, 'You have already disliked this video!')
            return redirect('post_detail', pk=video.id)
        else:
            video.videoUsersDisLiked.add(user)
        video.dislike()
        video.save()
        return redirect('post_detail', pk=video.id)
    except:
        video = Video.objects.get(id=pk)
        messages.error(request, 'Something wrong with post')
        return redirect('post_detail', pk=video.id)

    context = {}
    return render(request, 'tube/videoDetail.html', context)


def authorPage(request):
    user = request.user
    author_posts = Video.objects.filter(post_author__username=user)
    filter = VideoFilter(request.GET, queryset=author_posts)

    context = {'author_posts': author_posts, 'filter': filter}
    return render(request, 'tube/author_posts.html', context)


def postCreatePage(request):
    user = request.user
    form = PostForm(request.POST)
    if request.method == 'POST':
        if user.has_perm('tube.change_post'):
            if form.is_valid():
                post = form.save()
                post.post_author = user
                post.save()
                return redirect('post_detail', pk=post.id)
            else:
                messages.error(request, 'Something wrong with post, please try again')
        else:
            messages.error(request, "You don't have permission!")

    context = {'form': form}
    return render(request, 'tube/post_create.html', context)


def repliesPage(request, pk):
    post = Video.objects.get(id=pk)
    comments = Comment.objects.filter(comment_post__id=post.id, comment_online=False)
    good_sign = request.POST.get('get_id')
    bad_sign = request.POST.get('delete_id')

    if good_sign is not None:
        id = good_sign
        comment = Comment.objects.get(id=id)
        comment.comment_online = True
        comment.save()

    elif bad_sign is not None:
        id = bad_sign
        comment = Comment.objects.get(id=id)
        comment.delete()

    context = {'comments': comments}
    return render(request, 'tube/post_replies.html', context)


def postUpdatePage(request, pk):
    post = Video.objects.get(id=pk)
    form = PostForm(instance=post)
    user = request.user
    if request.method == 'POST':
        if user.has_perm('tube.change_post'):
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('main_page')
            else:
                messages.error(request, "Something went wrong!")
        else:
            messages.error(request, "You don't have permission!")

    context = {'form': form}
    return render(request, 'tube/post_create.html', context)


def postDetailPage(request, pk):
    video = Video.objects.get(id=pk)
    comments = Comment.objects.filter(commentVideo__id=video.id)
    user = request.user
    author = Author.objects.get(authorName=video.videoAuthor.authorName)

    subscription = user.subscriptions.all()
    isSubscribeToChannelOfVideo = author.authorName in subscription
    print(isSubscribeToChannelOfVideo)
    if request.method == 'POST':
        if user.has_perm('tube.view_post'):
            comment = request.POST.get('text')
            Comment.objects.create(comment_text=comment, comment_user=user, comment_post=video)
            return redirect('post_detail', pk=video.id)
        else:
            messages.error("You don't have permission!")

    context = {'comments': comments, 'video': video, 'subscribe':isSubscribeToChannelOfVideo}
    return render(request, 'tube/videoDetail.html', context)


def subscribeVideos(request):
    user = request.user
    subscription = user.subscriptions.all()
    if subscription:
        videos = Video.objects.filter(videoAuthor__authorName__in=subscription)
    else:
        videos = ''

    context = {'videos':videos}
    # context = {}
    return render(request, 'tube/index.html', context)


def subscribeToChannel(request, channel):
    author = User.objects.get(email=channel)
    user = request.user
    subscription = user.subscriptions.all()
    if user not in subscription:
        user.subscriptions.add(author)
        user.save()
        return redirect('home')
    else:
        print(subscription)
        return redirect('home')

    return render(request, 'tube/index.html', {})


def unSubscribeToChannel(request, channel):
    author = User.objects.get(email=channel)
    user = request.user
    subscription = user.subscriptions.all()
    print(subscription)
    if author in subscription:
        user.subscriptions.remove(author)
        print('success')
        return redirect('home')
    return render(request, 'tube/index.html', {})
