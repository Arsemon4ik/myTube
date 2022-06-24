from django.urls import path

from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('api/users', views.getUsers)
]
