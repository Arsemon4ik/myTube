from django.urls import path, re_path
from . import views

urlpatterns = [
    path('<str:username>', views.ThreadView.as_view())
]