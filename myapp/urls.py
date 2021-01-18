from django.urls import path, include
from . import views
from django.conf import settings 
from django.conf.urls import url
from .routers import router

urlpatterns = [
    path('', views.home, name="home-page"),
    # url(r'^api/files$', views.files_list),
    # url(r'^api/files/(?P<pk>[0-9]+)$', views.file_detail),
    path('api/', include(router.urls)),
]
