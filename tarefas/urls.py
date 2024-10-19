from .views import index, get_login
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('login/', get_login, name='login'),
    path('home/', index, name='home'),
]
