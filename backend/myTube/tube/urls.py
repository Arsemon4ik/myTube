from django.urls import path

from . import views

urlpatterns = [
    path('', views.indexPage, name='home'),
    path('video/<int:pk>/', views.postDetailPage, name='post_detail'),
    path('video/<int:pk>/like', views.postLikePage, name='post_like'),
    path('video/<int:pk>/dislike', views.postDisLikePage, name='post_dislike'),
    # path('', views.getRoutes),
    # path('videos', views.getVideos),
    # path('videos/<int:pk>', views.getVideo)

]
