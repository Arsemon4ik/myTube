from django.urls import path

from . import views

urlpatterns = [
    path('', views.indexPage, name='home'),
    path('<int:pk>/', views.postDetailPage, name='post_detail'),
    # path('', views.getRoutes),
    # path('videos', views.getVideos),
    # path('videos/<int:pk>', views.getVideo)

]
