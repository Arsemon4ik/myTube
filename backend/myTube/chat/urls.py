from django.urls import path

from . import views

urlpatterns = [
    path('<str:username>', views.ThreadView.as_view(), name='chat')
]
