from django.urls import path, include
from . import views
from .routers import router

urlpatterns = [
    path('', views.home, name="home-page"),
    path('api/', include(router.urls)),
]
