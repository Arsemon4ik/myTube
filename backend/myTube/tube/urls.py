from django.urls import path

from . import views

urlpatterns = [
    path('', views.indexPage, name='home'),
    # path('', views.getRoutes),
    # path('videos', views.getVideos),
    # path('videos/<int:pk>', views.getVideo)


]
