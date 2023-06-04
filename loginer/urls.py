from django.urls import path

from .views import profile, login, register, logout_view

app_name = 'loginer'

urlpatterns = [
    path('', profile, name='profile'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
]