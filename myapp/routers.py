from rest_framework import routers
from .viewsets import DataViewSet

router = routers.DefaultRouter()

router.register(r'files', DataViewSet,basename='data')