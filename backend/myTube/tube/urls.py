from django.urls import path

from . import views

urlpatterns = [
    path('', views.indexPage, name='home'),
    path('video/<int:pk>/', views.postDetailPage, name='post_detail'),
    path('video/<int:pk>/like', views.postLikePage, name='post_like'),
    path('video/<int:pk>/dislike', views.postDisLikePage, name='post_dislike'),
    path('video/subscription', views.subscribeVideos, name='subscription'),
    path('subscribe/<str:channel>', views.subscribeToChannel, name='subscribe'),
    path('unsubscribe/<str:channel>', views.unSubscribeToChannel, name='unsubscribe'),

    # path('', views.getRoutes),
    # path('videos', views.getVideos),
    # path('videos/<int:pk>', views.getVideo)

]
