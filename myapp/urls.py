from django.urls import path, include
from . import views
from django.conf import settings 
from django.conf.urls import url
from .routers import router
# from .views import ProductSearchViewSet 

urlpatterns = [
    path('', views.home, name="home-page"),
    path('search/', views.search, name="search-page"),
    path('api/', include(router.urls)),
]
