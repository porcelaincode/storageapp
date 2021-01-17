from django.urls import path, include
from . import views
from django.conf import settings 
from .routers import router

urlpatterns = [
    path('', views.home, name="home-page"),
    path('api/', include(router.urls)),
]
