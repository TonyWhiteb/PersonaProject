from rest_framework import viewsets, filters
from uploadimage_rest.serializers import UploadedImageSerializer # import our serializer
from uploadimage.models import UploadedImage # import our model


class UploadedImagesViewSet(viewsets.ModelViewSet):
    queryset = UploadedImage.objects.all()
    serializer_class = UploadedImageSerializer