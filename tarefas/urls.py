from .views import index
from django.urls import path, include

urlpatterns = [
    path('', index, name='index'),
    path('contas/', include('allauth.urls')),
    path('home/', index, name='home'),
]
