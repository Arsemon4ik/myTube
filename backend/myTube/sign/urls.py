from django.urls import path

from . import views

urlpatterns = [
    # path('', views.getRoutes),
    # path('users', views.getUsers)
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.registerPage, name='signup'),
    path('profile/', views.profilePage, name='profile'),
]
