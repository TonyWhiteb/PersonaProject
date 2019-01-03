from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from uploadimage_rest.viewsets import UploadedImagesViewSet

router = routers.DefaultRouter()
router.register('images', UploadedImagesViewSet, 'images')
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    # path('', include(router.urls)),
]